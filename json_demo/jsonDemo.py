#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/23 11:13
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : jsonDemo.py
@Software : PyCharm Community
"""

import json

d = dict(name='Bob', age=20, score=88)
json_str = json.dumps(d)
print(json_str)

d1 = json.loads(json_str)
print(d1)
