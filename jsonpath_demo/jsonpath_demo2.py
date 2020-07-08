#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/6/3 18:55
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : jsonpath_demo2.py
@Software : PyCharm Community
"""

import jsonpath
import json
#将json格式字符串转化为python对象
obj=json.load(open('book.json','r',encoding='utf8'))
#print(obj)

#写【0】代表查询第一本书的作者
ret=jsonpath.jsonpath(obj,'$.store.book[*].author')
#print(ret)

#查找store下面所有节点 注意 $.store 与 $.store.* 的区别
ret=jsonpath.jsonpath(obj,'$.store.*')
#print(ret)

#store里面所有东西的price
ret=jsonpath.jsonpath(obj,'$.store..price')
#print(ret)

# book下面第三个book,返回的是一个列表
ret1=jsonpath.jsonpath(obj,'$.store.book[2]')
ret2=jsonpath.jsonpath(obj,'$..book[2]')
#print(ret1)
#print(ret2)

# book下面最后个book,返回的是一个列表
ret=jsonpath.jsonpath(obj,'$..book[(@.length-1)]')
#print(ret)

#book下面前两本书
ret=jsonpath.jsonpath(obj,'$..book[0,1]')
#用切片也可以
#ret=jsonpath.jsonpath(obj,'$..book[:2]')
#print(ret)

#查找所有的包含isbn这个键的所有book
ret=jsonpath.jsonpath(obj,'$..book[?(@.isbn)]')
#print(ret)

#查找价格低于10的所有书
ret=jsonpath.jsonpath(obj,'$..book[?(@.price<10)]')
#print(ret)
