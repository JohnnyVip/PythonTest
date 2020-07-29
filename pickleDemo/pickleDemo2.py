#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/23 10:56
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : pickleDemo2.py
@Software : PyCharm Community
"""

import pickle

d = dict(name='Bob', age=20, score=88)
dict_bytes = pickle.dumps(d)
f = open('dump_1.txt', 'wb')
f.write(dict_bytes)
f.close()
print(dict_bytes)
