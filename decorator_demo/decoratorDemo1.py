#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/17 16:10
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : decoratorDemo1.py
@Software : PyCharm Community
"""

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        #print('call %s():' % func.__name__)
        #print('args = {}'.format(*args))
        return func(*args, **kwargs)
    return wrapper

@log
def test(p):
    print(test.__name__ + " param: " + p)

test("I'm a param")