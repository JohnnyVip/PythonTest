#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/7/23 11:26
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : single_demo2.py
@Software : PyCharm Community
"""


class SingleInstance:
    def __init__(self, *args, **kwargs):
        self.arg = args
        self.kwargs = kwargs

    def __call__(self, cls):
        def new(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = object.__new__(cls)
            return cls.instance

        cls.__new__ = new
        return cls

# A = SingleInstance().__call__(A)
@SingleInstance()
class A:
    pass