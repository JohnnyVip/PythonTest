#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/10/8 11:01
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : pytest_demo1.py
@Software : PyCharm Community
"""

#conftest.py的内容
import pytest

@pytest.fixture(scope="function",autouse=True)
def foo():
    print(" function setup")
    #yield 100
    print(" function teardown")

#test_1540.py的内容
import pytest

def inc(x):
    return x + 1

def test_answer_1():
    assert inc(3) == 5

def test_answer_2(foo):
    #print(foo)
    assert inc(98) == foo

if __name__ == '__main__':
    pytest.main()
