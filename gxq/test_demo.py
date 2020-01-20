#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/10/31 18:13
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : test_demo.py
@Software : PyCharm Community
"""


class TestDemo():
    a = 1

    def __init__(self,a):
        self.a = a

    def func(self):
        print(self.a)

print(TestDemo.a.func())