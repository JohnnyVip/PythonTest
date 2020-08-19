#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/8/18 14:26
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : namedtuple_demo1.py
@Software : PyCharm Community
"""

from collections import namedtuple
Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
print(perry[0])
print(type(perry))
print(perry.name,perry.age,perry.type)
print(dir(perry))