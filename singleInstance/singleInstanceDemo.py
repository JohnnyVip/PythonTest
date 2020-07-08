#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/20 13:52
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : singleInstanceDemo.py
@Software : PyCharm Community
"""


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kw):
        '''object将__new__()方法定义为静态方法，并且至少需要传递一个参数cls
           cls表示需要实例化的类，此参数在实例化时由Python解释器自动提供
        '''
        if not cls._instance:
            print('create Singleton instance')
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)  # super函数干啥的。。
        else:
            print('instance Singleton exists')
        return cls._instance


class A(Singleton):
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            print ('create A instance')
            cls._instance = super(A, cls).__new__(cls, *args, **kw)

        else:
            print ('instance A exists')
        return cls._instance

    def __init__(self):
        print('A')

A1 = A()
A2 = A()


