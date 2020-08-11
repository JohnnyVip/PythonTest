#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/8/4 17:36
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : permutation_demo.py
@Software : PyCharm Community
"""


def permutations(arr, position, end):
    if position == end:
        print(arr)

    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position + 1, end)
            arr[index], arr[position] = arr[position], arr[index]


arr = ["a", "b", "c"]
permutations(arr, 0, len(arr))