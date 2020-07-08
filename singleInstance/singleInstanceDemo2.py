#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/20 14:14
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : singleInstanceDemo2.py
@Software : PyCharm Community
"""


def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            print('create instance')
            _instance[cls] = cls(*args, **kargs)
        else:
            print('instance exits')
        return _instance[cls]

    return _singleton

@Singleton # A = Singleton(A)
class A(object):
    def __init__(self, x=0):
        self.x = x

a1 = A(2)
a2 = A(3)
