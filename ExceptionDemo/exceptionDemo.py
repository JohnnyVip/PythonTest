#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/22 15:42
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : exceptionDemo.py
@Software : PyCharm Community
"""

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')

print("END---1")

print("==========================")

try:
    print('try...')
    r = int("a123")
    print('result:', r)
except ValueError as e:
    print('except:', e)
finally:
    print('finally...')

print('END---2')
