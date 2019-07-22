# !/usr/bin/env python3
# -*- coding:utf-8 -*-
from contextlib import contextmanager

'''
代码的执行顺序是：
1. with语句首先执行yield之前的语句，因此打印出<h1>；
2. yield调用会执行with语句内部的所有语句，因此打印出hello和world；
3. 最后执行yield之后的语句，打印出</h1>。
   因此，@contextmanager让我们通过编写generator来简化上下文管理。
'''
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")
