#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/6/2 19:24
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : enumuate_demo.py
@Software : PyCharm Community
"""

string = ['a','b','c','d']

for i,s in enumerate(string):
    if not i:
        print(s)
    else:
        print("===========")