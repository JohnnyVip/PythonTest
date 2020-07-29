#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/22 15:49
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : exceptionDemo3.py
@Software : PyCharm Community
"""

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

main()
