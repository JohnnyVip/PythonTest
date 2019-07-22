# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# def count():
#     fs = []
#     for i in range(1,4):
#         def fn():
#             return i*i
#         fs.append(fn)
#     return fs
#
# f1,f2,f3 = count()
#
# print(f1(),f2(),f3())

def count():

    def f(i): #i是一个局部变量，每一次调用f，i均是不同的
        def g():
            return i*i
        return g

    fs = []

    for i in range(1,4):
        fs.append(f(i))

    return fs

f1,f2,f3 = count()
print(f1(),f2(),f3())