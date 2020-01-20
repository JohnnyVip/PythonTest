#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/17 17:37
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : decoratorParaDemo2.py
@Software : PyCharm Community
"""

import functools

def log_with_param(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('call %s():' % func.__name__)
            print('args = {}'.format(*args))
            print('log_param = {}'.format(text))
            return func(*args, **kwargs)

        return wrapper

    return decorator

# test_with_param = log_with_parm(text)(log_with_param)
@log_with_param("param")
def test_with_param(p):
    print(test_with_param.__name__)


# 带参数装饰器的解析：
# 传入装饰器的参数，并接收返回的decorator函数
decorator = log_with_param("param")
# 传入test_with_param函数
wrapper = decorator(test_with_param)
# 调用装饰器函数
wrapper("I'm a param")