#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/6/11 13:07
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : test_self.py
@Software : PyCharm Community
"""

class Test:

    a = 2

    def test01(self):
        Test.a = 1

    def test02(self):
        print(Test.a)


t = Test()
t.test01()
t.test02()
