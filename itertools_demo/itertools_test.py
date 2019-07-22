# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import itertools
naturals = itertools.count(1)

for n in naturals:
    print(n)
    if(n==100):
        break

cs = itertools.cycle('ABC')

i = 1
for ch in cs:
    print(ch)
    i += 1
    if(i == 100):
        break

ns = itertools.repeat('A', 3)

for ch in ns:
    print(ch)

for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))