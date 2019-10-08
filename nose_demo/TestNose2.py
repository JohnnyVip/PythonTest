#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/24 10:41
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : TestNose2.py
@Software : PyCharm Community
"""

from nose import with_setup


def my_setup_function():
    print('this is my_setup_function')


def my_teardown_function():
    print('this is my_teardown_function')


@with_setup(my_setup_function, my_teardown_function)
def test_numbers_3_4():
    print('success')
    assert 3 * 4 == 12
'''
#如果不喜欢使用装饰器，也可以直接赋属性值：
test_numbers_3_4.setup = my_setup_function
test_numbers_3_4.teardown = my_teardown_function
'''
