# !/usr/bin/env python3
# -*- coding:utf-8 -*-

from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)


