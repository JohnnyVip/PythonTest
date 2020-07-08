#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/20 14:33
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : superDemo.py
@Software : PyCharm Community
"""

class A:
    def fun(self):
        print('A.fun')

class B(A):
    def fun(self):
        super(B , self).fun()
        print('B.fun')

class C(A):
    def fun(self):
        super(C , self).fun()
        print('C.fun')

class D(B, C):
    def fun(self):
        super(D , self).fun()
        print('D.fun')

print(D.mro())

D().fun()

'''
print(D.mro())：[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
super调用过程：
先执行D中fun方法, 其中的fun有super调用，每执行到一次super时，
都会从__mro__方法元组中顺序查找搜索。所以先调用B中的fun方法，在fun方法中又有super调用，这个时候就就根据__mro__表去调用C的fun方法，
然后在C中又有super调用，这个就根据mro表又去调用A中的fun方法，到A结束了不再有super调用.后面都知道了
'''

