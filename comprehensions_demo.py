#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/7/8 16:32
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : comprehensions_demo.py
@Software : PyCharm Community
"""

d = {'x': 'A', 'y': 'B', 'z': 'C' }

l = [x + '=' + y for x,y in d.items()]

print(l)