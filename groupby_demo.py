#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/8/13 13:34
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : groupby_demo.py
@Software : PyCharm Community
"""

from itertools import groupby

'''
在数据统计时，经常需要用分组统计的时候，
如果是表格类数据可以用Pandas实现，
不过Python自身也提供给了gropuby，
有点不同的是它只会对相邻相同KEY的元素做聚合，这点需要注意。
'''

# 文章ID、文章分类
datas = [
    {"id":101, "category":"Python"},
    {"id":102, "category":"Java"},
    {"id":103, "category":"C++"},
    {"id":104, "category":"Python"},
    {"id":105, "category":"Python"},
    {"id":106, "category":"Java"}
]

# 排序
datas = sorted(datas, key=lambda x:x["category"])

# 执行聚合
result = groupby(datas, key=lambda x : x["category"])

# 用字典的方式输出
for key, values in result:
    print(key, list(values))
