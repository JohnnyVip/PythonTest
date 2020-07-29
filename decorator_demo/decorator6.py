#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/7/23 14:01
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : decorator6.py
@Software : PyCharm Community
"""
import datetime
from functools import wraps

# 需求
'''
有这样一类函数func可以被装饰器A和B进行装饰，但是有个规则：白天只能被A装饰，夜间只能被B装饰。请实现这样的装饰器。
效果：白天打印日志-现在是白天，装饰器A被调用了；夜间打印日志-现在是夜间，装饰器B被调用了。
例如：
    @A
    @B
    def func():
        pass
'''


def get_day_or_night() -> int:
    """
    获取当前小时函数
    :return:
    """
    hour = datetime.datetime.now().hour
    return hour


def A(func):
    if 6 <= get_day_or_night() < 18:
        @wraps(func)
        def warpper_func(*args,**kwargs):
            print("现在是白天，装饰器A被调用了")
            return func(*args,**kwargs)
        return warpper_func
    else:
        return func


def B(func):
    if not 6 <= get_day_or_night() < 18:
        @wraps(func)
        def warpper_func(*args,**kwargs):
            print("现在是夜间，装饰器B被调用了")
            return func(*args,**kwargs)
        return warpper_func
    else:
        return func


# func=A(B(func1))
@A
@B
def func1():
    print("func1 执行了")

# func=B(A(func2))
@B
@A
def func2():
    print("func2 执行了")


func1()

func2()