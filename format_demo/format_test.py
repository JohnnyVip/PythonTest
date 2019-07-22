#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/19 17:25
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : format_test.py
@Software : PyCharm Community
"""

"{} {}".format("hello", "world")  # 不设置指定位置，按默认顺序
'hello world'

"{0} {1}".format("hello", "world")  # 设置指定位置
'hello world'

"{1} {0} {1}".format("hello", "world")  # 设置指定位置
'world hello world'

print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

#通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

#通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)

print('value 为: {0.value}'.format(my_value))  # "0" 是可选的