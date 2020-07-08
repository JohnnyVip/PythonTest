#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/7/8 14:47
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : kw_demo.py
@Software : PyCharm Community
"""

def person(name, age, *args, city, job):
    print(name, age, args, city, job)

person('Jack', 24, 'Beijing', 'Engineer',city='hefei',job='baomu')

