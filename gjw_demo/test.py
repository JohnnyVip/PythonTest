#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/15 20:22
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : test.py
@Software : PyCharm Community
"""
from collections import Iterable


def square(x):  # 计算平方数
    return int(x) ** 2

f = map(square, "123456")  # 计算列表各个元素的平方

print(list(f))

