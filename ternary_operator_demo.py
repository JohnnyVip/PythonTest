#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/7/8 16:49
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : ternary_operator_demo.py
@Software : PyCharm Community
"""
# x if x % 2 == 0 else -x 是一个三目表达式
l = [x if x % 2 == 0 else -x for x in range(1, 11)]

print(l)