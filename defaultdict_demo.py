#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/8/13 13:21
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : defaultdict_demo.py
@Software : PyCharm Community
"""

from collections import defaultdict

dint = defaultdict(int)
dint["a"] += 3
dint["b"] += 4

print(dint)

dlist = defaultdict(list)
dlist["a"].append(1)
dlist["a"].extend([2,3,4])
dlist["a"].insert(1,'b')

print(dlist)