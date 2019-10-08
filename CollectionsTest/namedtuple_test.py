# !/usr/bin/env python3
# -*- coding:utf-8 -*-

from collections import namedtuple

Circle1 = namedtuple('Circle',"x y r")
c = Circle1(1,2,3)

print(c)
print(c.x,c.y,c.r)

Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)

print(p)
print(isinstance(p, Point))
print(isinstance(p, tuple))







