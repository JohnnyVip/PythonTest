#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/8/13 13:56
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : greenlet_demo.py
@Software : PyCharm Community
"""

import greenlet

def test1():
    print(1)
    g2.switch()
    print(2)

def test2():
    print(3)
    g1.switch()
    print(4)

g1 = greenlet.greenlet(test1)
g2 = greenlet.greenlet(test2)

g1.switch()