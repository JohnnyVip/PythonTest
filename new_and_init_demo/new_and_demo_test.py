#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class A(object):
    def __init__(self):
        print("init %s" % self)

    def __new__(cls, *args):
        print("new %s" % cls)
        obj = object.__new__(cls) #这里的cls是类A的引用
        print(cls is A)
        print(obj)
        return obj
A()


