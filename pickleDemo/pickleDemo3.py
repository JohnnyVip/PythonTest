#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/23 10:59
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : pickleDemo3.py
@Software : PyCharm Community
"""
import pickle

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)
