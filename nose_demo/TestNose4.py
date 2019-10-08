#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/24 10:59
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : TestNose4.py
@Software : PyCharm Community
"""

from nose import with_setup


def my_setup_function():
    print('this is my_setup_function')


def my_teardown_function():
    print('this is my_teardown_function')


# module
def setup_module(module):
    print("")  # this is to get a newline after the dots
    print("setup_module before anything in this file")


def teardown_module(module):
    print("teardown_module after everything in this file")


# function
@with_setup(my_setup_function, my_teardown_function)
def test_numbers_3_4():
    print('success')
    assert 3 * 4 == 12


@with_setup(my_setup_function, my_teardown_function)
def test_numbers_2_3():
    print('fail')
    assert 2 + 3 == 5

# 如果不喜欢使用装饰器，也可以直接赋属性值：
# test_numbers_3_4.setup = my_setup_function
# test_numbers_3_4.teardown = my_teardown_function

# class
class TestUM:

    def setup(self):
        print("TestUM:setup() before each test method")

    def teardown(self):
        print("TestUM:teardown() after each test method")

    @classmethod
    def setup_class(cls):
        print("setup_class() before any methods in this class")

    @classmethod
    def teardown_class(cls):
        print("teardown_class() after any methods in this class")

    def test_numbers_5_6(self):
        print('test_numbers_5_6()  <============================ actual test code')
        assert 5 * 6 == 30

    def test_strings_b_2(self):
        print('test_strings_b_2()  <============================ actual test code')
        assert 'b' * 2 == 'bb'
