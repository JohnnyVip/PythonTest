# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
参数组合:
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
比如定义一个函数，包含上述若干种参数：
虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。

*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict
'''

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
#f1(c=3,b=1,d=4,a=2,'e','f') error
#f1('e','f',c=3,b=1,d=4,a=2,'e','f') error
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)