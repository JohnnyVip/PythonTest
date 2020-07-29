#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/23 14:46
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : noLockDemo.py
@Software : PyCharm Community
"""

import time, threading

# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
