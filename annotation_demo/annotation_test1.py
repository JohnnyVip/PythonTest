#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/19 16:11
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : annotation_test1.py
@Software : PyCharm Community
"""

import inspect

def foobar(a: 1+1) -> 2 * 2:
    return a

sig = inspect.signature(foobar)

print(sig.parameters)

print(foobar.__annotations__)

print(foobar(3))

