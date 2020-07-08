#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/22 17:17
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : IODemo.py
@Software : PyCharm Community
"""

from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
