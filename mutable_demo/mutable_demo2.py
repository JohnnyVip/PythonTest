#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/8/17 18:08
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : mutable_demo2.py
@Software : PyCharm Community
"""


def add_to(num, target=[]):
    target.append(num)
    return target

# Output: [1]
print(add_to(1))

# Output: [1, 2]
print(add_to(2))

# Output: [1, 2, 3]
print(add_to(3))
