#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Base(object):
    def __init__(self,a):
        self.__a = a
    pass

class Derived(Base):
    def __init__(self,a,b):
        Base.__init__(self,a)
        self.__b = b

    def show(self):
        print(self.__a,self.__b)

d = Derived(1,2)
