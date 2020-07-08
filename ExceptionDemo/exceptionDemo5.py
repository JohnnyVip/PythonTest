#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/22 16:01
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : exceptionDemo5.py
@Software : PyCharm Community
"""
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        # raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型
        raise

bar()

# raise 转化异常错误
# try:
#     10 / 0
# except ZeroDivisionError:
#     raise ValueError('input error!')

