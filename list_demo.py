#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/5/28 13:51
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : list_demo.py
@Software : PyCharm Community
"""
list1 = []
for i in range(10):
    list1.append(i)

print(sorted(list1,reverse=True))