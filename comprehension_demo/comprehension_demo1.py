#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/8/18 15:02
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : comprehension_demo1.py
@Software : PyCharm Community
"""

mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase.keys()}
print(mcase_frequency)