#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/23 10:26
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : dictDemo2.py
@Software : PyCharm Community
"""

d = dict(name='Bob', age=20, score=88)
print(d)
print(d.get("name"))
print(d.get("sex",'no key'))
