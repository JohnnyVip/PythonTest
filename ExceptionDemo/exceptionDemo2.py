#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/22 15:48
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : exceptionDemo2.py
@Software : PyCharm Community
"""

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
