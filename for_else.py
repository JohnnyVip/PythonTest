#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/8/18 18:23
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : for_else.py
@Software : PyCharm Community
"""
'''
它会找出2到10之间的数字的因⼦。 现在是趣味环节了。 
我们可以加上⼀个附加的else语句块， 来抓住质数
'''
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')