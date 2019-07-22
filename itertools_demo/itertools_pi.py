# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import itertools
def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    g_odds = itertools.count(1,2)

    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    def get_odds(n,odds,L=None):
        if L is None:
            L = []
            for odd in odds:
                if(odd > 2*n-1):
                    break
                L.append(odd)
            return L

    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    def num_get(L1=None,L2=None):
        if L2 is None:
            L2 = []
            for n,odd in enumerate(L1):
                num = (4/odd)*(-1)**n
                L2.append(num)
            return L2

    # step 4: 求和:
    odds = get_odds(N,g_odds)
    return sum(num_get(odds))


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')