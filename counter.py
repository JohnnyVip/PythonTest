# !/usr/bin/env python3
# -*- coding:utf-8 -*-

#python引用变量的顺序： 当前作用域局部变量->外层作用域变量->当前模块中的全局变量->python内置变量
#global 和 nonlocal 的作用域
def createCounter():
    i = 0
    def counter():
        nonlocal i
        i += 1
        return i
    return counter

counterA = createCounter()

print(counterA(),counterA(),counterA(),counterA(),counterA())