#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
init 函数隐式被子类调用，子类可以重写父类的init
'''

class Base(object):
    def __init__(self,a):
        print("init run ...")
        self.a = a

class Derive(Base):
    def __init__(self,a,b):
        Base.__init__(self,a)
        self.b = b

    pass

d = Derive(0,1)

print(d.a,d.b)