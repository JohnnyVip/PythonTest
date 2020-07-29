#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/20 17:03
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : superDemo7.py
@Software : PyCharm Community
"""


class Parent(object):
    def __init__(self, name):
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束被调用')


class Son1(Parent):
    def __init__(self, name, age):
        print('Son1的init开始被调用')
        self.age = age
        super().__init__(name)  # 单继承不能提供全部参数
        print('Son1的init结束被调用')


class Grandson(Son1):
    def __init__(self, name, age, gender):
        print('Grandson的init开始被调用')
        super().__init__(name, age)  # 单继承不能提供全部参数
        print('Grandson的init结束被调用')


gs = Grandson('grandson', 12, '男')
print('姓名：', gs.name)
print('年龄：', gs.age)
