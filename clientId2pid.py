#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/5/15 13:39
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : clientId2pid.py
@Software : PyCharm Community
"""

def client_id_to_pid():
    """
    批量client id换取pid
    :return:
    """
    # 打开文件

    f = open("clientId.txt", "r")

    for line in f.readlines():  # 依次读取每行

        line = line.strip()  # 去掉每行头尾空白



    # 关闭文件

    f.close()
    return 0
    pass

client_id_to_pid()