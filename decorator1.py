# !/usr/bin/env python3
# -*- coding:utf-8 -*-

def wrap(func):
    def wrapper(*args, **kw):
        """wrap func: call_it"""
        print('before call')
        return func(*args, **kw)
    return wrapper

@wrap # wrapped = wrap(wrapped)
def wrapped():
    """test wrapped"""
    print("hello world")


from functools import update_wrapper

def wrap2(func):
    def call_it(*args, **kw):
        """wrap func: call_it2"""
        print('before call')
        return func(*args, **kw)
    return update_wrapper(call_it, func)

@wrap2
def wrapped2():
    """test wrapped2"""
    print('hello world2')

if __name__ == '__main__':
    wrapped()
    print(wrapped.__name__)
    print(wrapped.__doc__)

    print('*'*20)

    wrapped2()
    print(wrapped2.__name__)
    print(wrapped2.__doc__)


