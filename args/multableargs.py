#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/21 13:46
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : multableargs.py
@Software : PyCharm Community
"""

def person1(name, age, *args, city, job):
    print(name, age, args, city, job)
    return None

def person2(name, age, *, city, job):
    print(name, age, city, job)
    return None

person1('Jack', 24, city='Beijing', job='Engineer')

person2('Jack', 24, city='Beijing', job='Engineer')
