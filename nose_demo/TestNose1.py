#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/24 10:16
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : TestNose1.py
@Software : PyCharm Community
"""

def setUpModule():
    print("=======setUpModule=======")

def tearDownModule():
    print("=======tearDownModule=======")

class TestNose1:
    @classmethod
    def setUpClass(cls):
        print("=============setUpClass==========")

    @classmethod
    def tearDownClass(cls):
        print("=============tearDownClass=========")

    def setUp(self):
        print("===================setUp=======")

    def tearDown(self):
        print("===================tearDown======")

    def test1(self):
        print("=========================test1=====")

    def test2(self):
        print("=========================test2=====")

    def func(self):
        print("====func====")

    def test3(self):
        print("=========================test3=====")