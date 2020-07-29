#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/21 18:25
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : sortedDemo.py
@Software : PyCharm Community
"""

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_name)
L3 = sorted(L,key=by_score,reverse=False)
L4 = sorted(L,key=by_score,reverse=True)
print(L2)
print(L3)
print(L4)