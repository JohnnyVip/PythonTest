# -*- coding:utf-8 -*-

"""
    实现 TFTP 上传与下载功能
    需要配合tftpd 软件测试
"""

from socket import *
import struct
import sys


class DownloadClient:
    """
        下载基本流程：
        --------------------------------------
        客户端(Client)         服务端(Server)
        --------------------------------------
        读写请求          --->
                        <---     数据包[0]
        ACK[0]          --->
                        <---     数据包[1]
        ACK[1]          --->
        ....
        --------------------------------------

        操作码     功能
        --------------------------------------
        1           读请求，即下载
        2           写请求，即上传
        3           表示数据包，即Data
        4           确认码，即ACK
        5           错误
        --------------------------------------
    """
    def __init__(self):
        # 读取参数
        if len(sys.argv) != 4:
            print("-" * 30)
            print("Tips:")
            print("python xxx.py 1 127.0.0.1 test.png")
            print("-" * 30)
            exit()
        else:
            self.mid = sys.argv[1]       # 执行的方法，1下载或2上传
            self.remoteIp = sys.argv[2]  # 服务器IP
            self.filename = sys.argv[3]     # 下载文件名

        # 创建socket实例
        self.socketClient = socket(AF_INET, SOCK_DGRAM)
        self.socketClient.bind(('', 7788))

    def start(self):
        """启动执行"""
        if self.mid == "1":
            self.download()
        elif self.mid == "2":
            self.upload()
        else:
            print(self.mid)
            print("参数输入错误 [python 脚本名 方法id(1下载，2上传) 服务器IP 文件名]：python xxx.py 1 127.0.0.1 test.png")
            exit()

    def download(self):
        """ TFTP 下载"""
        print("下载启动...")

        # 构建下载请求数据
        # 第一个参数 !H7sb5sb = "!H"+str(len(filename))+"sb5sb"
        filenameLen = str(len(self.filename))
        cmdBuf = struct.pack(("!H%ssb5sb" % filenameLen).encode("utf-8"), 1, self.filename.encode("utf-8"), 0, b"octet", 0)

        # 发送下载文件请求数据到指定服务器
        self.socketClient.sendto(cmdBuf, (self.remoteIp, 69))

        # self.show()

        locPackNum = 0  # 请求包号
        saveFile = ''   # 保存文件句柄
        while True:
            recvData, recvAddr = self.socketClient.recvfrom(1024)
            recvDataLen = len(recvData)

            # 解包
            cmdTuple = struct.unpack(b"!HH", recvData[:4])
            cmd = cmdTuple[0]   # 指令
            curPackNum = cmdTuple[1]    # 当前包号

            if cmd == 3:    # 是否为数据包
                if curPackNum == 1:
                    # 以追加的方式打开文件
                    saveFile = open(self.filename, "ab")

                # 包编号是否和上次相等
                if locPackNum + 1 == curPackNum:
                    saveFile.write(recvData[4:])    # 写入数据
                    locPackNum += 1

                    # 发送ACK应答
                    ackBuf = struct.pack(b"!HH", 4, locPackNum)
                    self.socketClient.sendto(ackBuf, recvAddr)

                    print("(%d)次接收到数据" % locPackNum)

                # 确认为最后一个包
                if recvDataLen < 516:
                    saveFile.close()
                    print("已经下载完成")
                    break

            elif cmd == 5:  # 是否为错误应答
                print("error num:%d" % curPackNum)
                break

    def upload(self):
        """TFTP 上传"""
        print("上传启动...")

        # 1、发送读请求
        filenameLen = str(len(self.filename))
        cmdBuf = struct.pack(("!H%ssb5sb" % filenameLen).encode("utf-8"), 2, self.filename.encode("utf-8"), 0, b"octet", 0)

        self.socketClient.sendto(cmdBuf, (self.remoteIp, 69))

        localPackNum = 1    # 本地包号
        sendFile = ''   # 文件句柄
        while True:
            # 2、接收回复
            recvData, recvAddr = self.socketClient.recvfrom(1024)

            # 3、解包
            cmdTuple = struct.unpack(b"!HH", recvData[:4])
            cmd = cmdTuple[0]  # 指令
            curPackNum = cmdTuple[1]  # 当前包号

            # print(recvData)

            if cmd == 4:
                # 打开并读取文件
                if curPackNum == 0:
                    sendFile = open(self.filename, "rb")

                # ACK应答的包号是否与本地的一样
                if localPackNum - 1 == curPackNum:
                    # 4、读取 512 byte数据
                    sendData = sendFile.read(512)

                    # 判断文件是否读取完成
                    if len(sendData) <= 0:
                        sendFile.close()
                        print("上传完成")
                        break

                    # 5、打包发送数据
                    sendDataBuf = struct.pack(b"!HH512s", 3, localPackNum, sendData)
                    self.socketClient.sendto(sendDataBuf, recvAddr)

                    # 打印过程
                    print("(%d)次已发送,数据长度:%d" % (localPackNum, len(sendData)))
                    localPackNum += 1

            elif cmd == 5:
                # sendFile.close()
                print("error num:%d" % curPackNum)
                break

    def show(self):
        """测试打印数据"""
        recvData = self.socketClient.recvfrom(1024)
        print(recvData)
        exit()


if __name__ == "__main__":
    demo = DownloadClient()
    demo.start()