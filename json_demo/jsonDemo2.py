#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/23 11:29
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : jsonDemo2.py
@Software : PyCharm Community
"""

import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))