#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/7/23 11:27
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : call_demo.py
@Software : PyCharm Community
"""


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print ('My name is %s...' % self.name)
        print ('My friend is %s...' % friend)

p = Person('yaoqiang','male')
p('cheng')