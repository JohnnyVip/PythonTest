#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/19 18:34
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : with_demo.py
@Software : PyCharm Community
"""

class Sample:
    def __enter__(self):
        print("In __enter__()")
        return "Foo"

    def __exit__(self, type, value, trace):
        print ("In __exit__()")

def get_sample():
    return Sample()

with get_sample() as sample:
    print("sample:", sample)
