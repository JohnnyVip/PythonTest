#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/4/17 17:20
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : sshDemo.py
@Software : PyCharm Community
"""
# -*- coding:utf8 -*-
# 执行hbase shell指令

import paramiko


class SSHCommand(object):
    """ssh 连接类"""

    host = "172.28.200.203"
    user = "hadoop"
    pwd = "fz_Hadoop"

    def ssh_connect(self, ip, port, username, password, command):
        """
        :param ip:
        :param port:
        :param username:
        :param password:
        :param command:
        :return:
        """
        # 创建SSH对象
        self.client = paramiko.SSHClient()

        # 允许连接不在know_hosts文件中的主机
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 连接服务器
        self.client.connect(ip, port, username, password)

        # 将SSHClient建立连接的对象得到一个Transport对象，
        # 以Transport对象的exec_command()在服务端执行命令
        ssh_session = self.client.get_transport().open_session()
        if ssh_session.active:
            ssh_session.exec_command(command)
            receive = ssh_session.recv(1024)
            print(receive.decode('utf-8'))

    def ssh_command(self, command):
        """
        shell 指令
        :param command:
        :return:
        """
        # 将SSHClient建立连接的对象得到一个Transport对象，
        # 以Transport对象的exec_command()在服务端执行命令
        ssh_session = self.client.get_transport().open_session()
        if ssh_session.active:
            ssh_session.exec_command(command)
            receive = ssh_session.recv(1024)
            f = open('/home/result.txt', 'a')
            f.write(receive.decode('utf-8'))
        pass

    # 关闭连接
    # client.close()
if __name__ == '__main__':
    SSHCommand().ssh_command(command='ls')