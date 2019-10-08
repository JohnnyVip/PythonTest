#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/26 19:18
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : decorator.py
@Software : PyCharm Community
"""

def kwrap(func):
    print(func)
    def warpper(*args,**kwargs):
        print("=============before wrap==============")
        a = func(*args,**kwargs)
        print("=============after wrap===============")
        #return a
    return warpper

@kwrap
def funcx(*args,**kwargs):
    print("===============================add()==============")
    return str(args) + str(kwargs)

@kwrap
def funcy():
    pass

#print(funcx(1,2,a = 1,b = 2))

print(funcy(1))




