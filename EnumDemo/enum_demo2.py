#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/8/18 14:36
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : enum_demo2.py
@Software : PyCharm Community
"""

from collections import namedtuple
from enum import Enum


class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9
    # 依次类推
    # 但我们并不想关⼼同⼀物种的年龄， 所以我们可以使⽤⼀个别名
    kitten = 1 # (译者注： 幼⼩的猫咪)
    puppy = 2 # (译者注： 幼⼩的狗狗)

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type=Species.cat)
drogon = Animal(name="Drogon", age=4, type=Species.dragon)
tom = Animal(name="Tom", age=75, type=Species.cat)
charlie = Animal(name="Charlie", age=2, type=Species.kitten)

print(charlie.type == tom.type)
print(charlie.type)