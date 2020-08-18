#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/8/17 18:18
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : mutable_demo3.py
@Software : PyCharm Community
"""


def add_to(element, target=None):
    if target is None:
        target = []
        target.append(element)
        return target

print(add_to(42))
# Output: [42]
print(add_to(42))
# Output: [42]
print(add_to(42))
# Output: [42]