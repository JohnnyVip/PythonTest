#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/22 17:40
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : decorator4.py
@Software : PyCharm Community
"""

def log(func):
    def wrapper(*args,**kwargs):
        print(*args,**kwargs)
        print("call %s():"%func.__name__)
        return func(*args,**kwargs)
    return wrapper

@log
def now(num:tuple):
    print("2015-3-25")

now((1,2,3))



