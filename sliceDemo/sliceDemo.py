#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/22 14:28
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : sliceDemo.py
@Software : PyCharm Community
"""

class Fib(object):

    def __getitem__(self, n):

        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L




