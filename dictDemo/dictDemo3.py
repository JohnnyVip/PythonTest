#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/7/30 13:21
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : dictDemo3.py
@Software : PyCharm Community
"""

'''Python中创建字典的若干方法'''

# 通过dict函数创建。
a = dict(one=1,two=2,three=3)
print("a=",a)

# 直接赋值创建
b = {'one': 1, 'two': 2, 'three': 3}
print("b=",b)

# 先用zip函数处理两个列表，再用dict函数转为字典
c = dict(zip(["one","tw0","three"],[1,2,3]))
print("c=",c)

# 用dict函数把列表转为字典。
d = dict([('one',1),('two',2),('three',3)])
print("d=",d)

# 通过dict.fromkeys(),这种方法通常用来初始化字典.把value值设置成固定的默认初始值。
e = dict.fromkeys(['one','two','three'],6)
print("e=",e)

# 用字典推导式来构建字典
nums = [('one',1),('two',2),('three',3)]
f = {en:ch for en,ch in nums}
print("f=",f)
