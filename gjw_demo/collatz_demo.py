#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/25 20:10
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : collatz_demo.py
@Software : PyCharm Community
"""

def collatz(num):
    print(num)
    if num % 2 == 1:
        return 3* num + 1
    else:
        return num // 2

str_a = input('请输入一个数：')
a = int(str_a)

while True:
    a = collatz(a)
    if a == 1:
        break