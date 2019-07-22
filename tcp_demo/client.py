#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 服务器地址（主机，端口）
# 建立连接:要连接的那个server的ip,因为server在本地，所以ip就是127.0.0.1
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))

# for data in [b'Michael', b'Tracy', b'Sarah']:
#     # 发送数据:
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
# exit 退出程序
# s.send(b'exit')
# s.close()

while True:
    raw_data = input("请输入数据:")
    data = bytes(raw_data, encoding='utf-8')
    s.send(data)
    if raw_data != 'exit':
        print(s.recv(1024).decode('utf-8'))
    else:
        s.close()
        break
