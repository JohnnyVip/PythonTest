#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/29 9:23
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : recursion_test1.py
@Software : PyCharm Community
"""

line = [1,2,3,4,5,6]

def howmanyin(lst):
    if lst[1:]:
        print("me and the guys behind")
        return 1 + howmanyin(lst[1:])
    else:
        print("just me")
        return 1

print(howmanyin(line))