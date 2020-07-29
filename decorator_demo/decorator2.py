# !/usr/bin/env python3
# -*- coding:utf-8 -*-

from functools import wraps
from functools import update_wrapper


def log(text):
    def decorator(func):
        #@wraps(func)
        def wrapper(*args,**kw):
            """wrap func: call_it"""
            print('%s %s():' % (text, func.__name__))
            print('begin call')
            result = func(*args,**kw)
            print('end call')
            return result
        return update_wrapper(wrapper, func)
    return decorator

@log("execute") # now = log("execute")(now)
def now():
    """test now"""
    print("2015-3-25")

if __name__ == '__main__':
    now()
    print(now.__name__)
    print(now.__doc__)
