#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/21 11:27
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : default_args.py
@Software : PyCharm Community
"""

def ddd(a,b=[]):
    print(id(b))
    b.append(a)
    print(id(b))
    return b

print(ddd(1))
print(ddd(2,['a','b','c']))
print(ddd(3))
