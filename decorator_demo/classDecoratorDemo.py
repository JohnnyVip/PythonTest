#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/20 12:21
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : classDecoratorDemo.py
@Software : PyCharm Community
"""

from functools import wraps

def wrapper(func):
    @wraps(func)
    def inner(self,*args,**kwargs):
        # 此时的self是Person的实例对象
        self.name += "爱吃糖"
        # func ===>  printInfo
        ret = func(self,*args,**kwargs)
        return ret

    return inner


class Person(object):
    def __init__(self,name):
        self.name = name

    @wrapper
    def printInfo(self):
        print(self.name)

# printInfo ==> wraper(printInfo) ==> inner
Person("张三").printInfo()

# 张三爱吃糖
