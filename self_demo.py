#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/6/12 10:13
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : self_demo.py
@Software : PyCharm Community
"""

class TestSelf:

    def setup_class(cls):
        print(f"setup_class:{id(cls)}")
        print(f"TestSelf:{id(TestSelf)}")


    def test01(self):
        print(f"test01:{self}")

    def test02(self):
        print(f"test02:{self}")