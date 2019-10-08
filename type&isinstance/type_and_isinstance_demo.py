#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/24 13:36
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : type_and_isinstance_demo.py
@Software : PyCharm Community
"""

'''
isinstance() 与 type() 区别：

type() 不会认为子类是一种父类类型，不考虑继承关系。

isinstance() 会认为子类是一种父类类型，考虑继承关系。

如果要判断两个类型是否相同推荐使用 isinstance()。
'''
class A:
    pass

class B(A):
    pass

isinstance(A(), A)  # returns True
print(type(A()) == A) # returns True
isinstance(B(), A)  # returns True
print(type(B()) == A)  # returns False

# type:list
a = None

print(type(a))