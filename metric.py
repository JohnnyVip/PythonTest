# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import functools
import time

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):  #此时fast指向了wrapper,wrapper可以接受*args,**kw参数.
        '''wrap fn: call_it'''
        start = time.time()
        result = fn(*args,**kw)  #fn指向了fast,fn可以接受从wrapper传递过来的参数,此时的*args表示将元组args解绑,**kw表示将字典解绑.
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, end-start))
        return result  #将结果返回,因为此时的函数的返回值代表原fast的函数的返回值
    return wrapper

# 测试
@metric #fast = metric(fast)
def fast(x, y):
    time.sleep(0.0112)
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
else:
    print('测试成功！')