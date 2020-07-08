#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/7/8 15:40
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : Iterable_demo.py
@Software : PyCharm Community
"""

from collections import Iterable

print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance((1,3,4),Iterable))