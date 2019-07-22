# !/usr/bin/env python3
# -*- coding:utf-8 -*-

a = [1, 2, 3]
b = [4, 5, 6]

for _item in enumerate(zip(a, b)):
    print(_item)

seasons = ['Spring', 'Summer', 'Fall', 'Winter']

l = list(enumerate(seasons, start=1))   # 下标从 1 开始,默认从零开始
print(l)

for i,element in enumerate(seasons):
    print(i,element)