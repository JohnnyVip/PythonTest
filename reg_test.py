#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/4/13 13:12
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : reg_test.py
@Software : PyCharm Community
"""

def reg_dot_new_line(reg_str:str)->str:
    """取出 . and \n 之前内容"""

    start_index = reg_str.find(r'.')
    end_index = reg_str.find(r'\n')
    return reg_str[start_index + 1:end_index]
    pass

print(reg_dot_new_line(reg_str=".poieojewo\n"))