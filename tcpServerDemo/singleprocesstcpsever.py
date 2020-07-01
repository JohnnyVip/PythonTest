# coding:utf-8
from socket import *

# 1.创建服务器socket
sock = socket(AF_INET, SOCK_STREAM)

# 2.绑定主机和端口
addr = ('', 7788)
sock.bind(addr)

# 3. 设置最大监听数目，并发
sock.listen(10)

# 4. 设置成非阻塞
sock.setblocking(False)
# 保存客户端socket
clientAddrList = []

while True:
    try:
        clientSocket, clientAddr = sock.accept()
    except:
        pass
    else:
        print("一个新客户端到来：%s" % str(clientAddr))
        clientSocket.setblocking(False)
        clientAddrList.append((clientSocket, clientAddr))

    for clientSocket, clientAddr in clientAddrList:
        try:
            recvData = clientSocket.recv(1024)
        except:
            pass
        else:
            if len(recvData) > 0:
                print("%s:%s" % (str(clientAddr), recvData))
            else:
                clientSocket.close()
                clientAddrList.remove((clientSocket, clientAddr))
                print("%s 已经下线" % str(clientAddr))