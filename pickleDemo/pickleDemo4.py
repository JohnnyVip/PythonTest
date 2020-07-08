#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/23 11:02
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : pickleDemo4.py
@Software : PyCharm Community
"""

import pickle

d = dict(name='Bob', age=20, score=88)
dict_bytes = pickle.dumps(d)
d1 = pickle.loads(dict_bytes)
print(dict_bytes)
print(d1)
