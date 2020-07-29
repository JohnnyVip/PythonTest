#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/8/6 15:38
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : decorator.py
@Software : PyCharm Community
"""

class Animal():

    def __init__(self):
        print("__init__ run ===========================")

    def __call__(self, f):
        self.func = f
        self.func.__doc__ = f.__doc__
        self.afterCall()
        return self.func

    def afterCall(self):
        pass

class Cat(Animal):

    def afterCall(self):
        print("===============+++++++++++++++++================")

@Cat()
def func():
    '''
    测试函数
    :return:
    '''
    print('func run ...........')

func()
