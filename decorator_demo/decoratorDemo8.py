#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/21 19:49
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : decoratorDemo8.py
@Software : PyCharm Community
"""
import functools
import time


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start_time = time.time() #开始时间
        result = fn(*args, **kw) #执行fn函数
        stop_time = time.time() #结束时间
        gap = stop_time - start_time   #执行时间
        print('%s executed in %s ms' % (fn.__name__, gap*1000))
        return result
    return wrapper

# 测试
@metric # fast = metric(fast)
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')