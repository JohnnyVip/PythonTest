#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/7/16 14:37
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : dict_get_demo.py
@Software : PyCharm Community
"""

dict = {'Name': 'Runoob', 'Age': 27}

print ("Value : %s" %  dict.get('Age'))
print ("Value : %s" %  dict.get('Sex', "Never"))
print ("Value : %s" %  dict.get('yaoqiang', "我有1万亿美元"))

