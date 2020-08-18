#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/8/13 13:14
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : counter_demo.py
@Software : PyCharm Community
"""

import collections

data = ['a', 'b', 'c',
        'a', 'b', 'a']

counter = collections.Counter(data)

print(counter)

# 对已有的Counter可以新增内容
counter.update(['c', 'b', 'c', 'd', 'c'])

print(counter)

# 遍历
for key, value in counter.items():
    print(key, value)

# 找出频次最高的前三个
print(counter.most_common(3))