#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/20 13:25
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : classDecoratorDemo2.py
@Software : PyCharm Community
"""

import time

class Foo():
    def __init__(self, func):  # 初始化函数中传入函数对象的参数
        self._func = func

    def __call__(self):  # 定义__call__方法，直接实现装饰功能
        start_time = time.time()
        self._func()
        end_time = time.time()
        print('花费了 %.2f' % (end_time - start_time))

@Foo  # bar=Foo(bar)
def bar():
    print('bar函数的执行时间为：')
    time.sleep(2.5)

bar()  # bar=Foo(bar)()，没有嵌套关系了,直接执行Foo的 __call__方法，实现装饰功能
