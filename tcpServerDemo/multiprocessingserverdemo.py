from multiprocessing import Process
from socket import *


def recv_data(new_socket, client_info):
    print("客户端{}已经连接".format(client_info))
    # 接受数据
    raw_data = new_socket.recv(1024)
    while raw_data:
        print(f"收到来自{client_info}的数据：{raw_data}")
        raw_data = new_socket.recv(1024)
    new_socket.close()


def main():
    # 实例化socket对象
    socket_server = socket(AF_INET, SOCK_STREAM)
    # 设置端口复用
    socket_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 绑定IP地址和端口
    socket_server.bind(("", 7788))
    # 改主动为被动，监听客户端
    socket_server.listen(5)
    while True:
        # 等待连接
        new_socket, client_info = socket_server.accept()
        p = Process(target=recv_data, args=(new_socket, client_info))
        p.start()
        # 多进程会复制父进程的内存空间，所以父进程中new_socket也必须关闭
        new_socket.close()


if __name__ == '__main__':
    main()