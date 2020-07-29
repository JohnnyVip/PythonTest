#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/22 15:58
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : exceptionDemo4.py
@Software : PyCharm Community
"""

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
        pass

main()
print('END')

