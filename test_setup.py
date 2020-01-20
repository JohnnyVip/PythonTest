#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/12/16 16:45
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : test_setup.py
@Software : PyCharm Community
"""

# content of test_websites.py

'''
Setup/teardown in pytest, see https://docs.pytest.org/en/3.5.1/xunit_setup.html

Remarks:
1. setup/teardown的结对函数在测试进程中可以被调用多次的。
2. 如果setup函数在执行时失败或被skipped了，相应的tearDown函数不会被调用。
'''

import pytest

def setup_module(module):
    """
    这是一个module级别的setup，它会在本module(test_website.py)里
    所有test执行之前，被调用一次。
    注意，它是直接定义为一个module里的函数"""
    print("-------------- setup before module --------------")


def teardown_module(module):
    """
    这是一个module级别的teardown，它会在本module(test_website.py)里
    所有test执行完成之后，被调用一次。
    注意，它是直接定义为一个module里的函数"""
    print("-------------- teardown after module --------------")


class TestBaidu(object):
    def test_login(self):
        print("test baidu login function")
        assert True == True


class TestSohu(object):
    @classmethod
    def setup_class(cls):
        """ 这是一个class级别的setup函数，它会在这个测试类TestSohu里
        所有test执行之前，被调用一次.
        注意它是一个@classmethod
        """
        print("------ setup before class TestSohu ------")

    @classmethod
    def teardown_class(cls):
        """ 这是一个class级别的teardown函数，它会在这个测试
        类TestSohu里所有test执行完之后，被调用一次.
       注意它是一个@classmethod
       """
        print("------ teardown after class TestSohu ------")

    def setup_method(self, method):
        """ 这是一个method级别的setup函数，它会在这个测试
         类TestSohu里，每一个test执行之前，被调用一次.
        """
        print("--- setup before each method ---")

    def teardown_method(self, method):
        """ 这是一个method级别的teardown函数，它会在这个测试
         类TestSohu里，每一个test执行之后，被调用一次.
        """
        print("--- teardown after each method ---")

    def test_login(self):
        print("sohu login")
        assert True == True

    def test_logout(self):
        print("sohu logout")
        pytest.skip()
