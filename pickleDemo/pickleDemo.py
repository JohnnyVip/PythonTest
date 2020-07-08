#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/23 10:54
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : pickleDemo.py
@Software : PyCharm Community
"""
import pickle

d = dict(name='Bob', age=20, score=88)
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
