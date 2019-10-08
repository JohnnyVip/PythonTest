#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/8/8 17:10
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : break_demo.py
@Software : PyCharm Community
"""

_info = [{"stock_name":None,"2":2,"3":3},{"stock_name":1,"2":2,"3":3}]

def findcontext(_info):

    dictname = None

    for dictname in _info:
        if dictname['stock_name']:
            print(dictname)
            break

    return dictname

findcontext(_info)