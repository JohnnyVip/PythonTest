#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 引入sys 模块

import sys

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()