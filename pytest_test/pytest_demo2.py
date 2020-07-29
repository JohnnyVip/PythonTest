#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/10/8 11:28
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : pytest_demo2.py
@Software : PyCharm Community
"""

# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5
