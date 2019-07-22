# !/usr/bin/env python3
# -*- coding:utf-8 -*-

from functools import partial

int2 = partial(int,base = 2)

print(int2('100000'))
#这里存在很大的问题？？？,int的源码是什么样的？
print(int2('100000',base = 10)) #base是命名关键字参数吗？

kw = {'base':2}
print(int2('100000',**kw))

max2 = partial(max,10)

#args = (10,5,6,7)
print(max2(5,6,7))
