#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/8/17 18:06
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : mutable_demo1.py
@Software : PyCharm Community
"""

foo = ['hi']
print(foo)
# Output: ['hi']
bar = foo
bar += ['bye']
print(foo)
# Output: ['hi']
print(bar)
# Output: ['hi', 'bye']