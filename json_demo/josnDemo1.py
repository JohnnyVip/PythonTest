#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/23 11:27
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : josnDemo1.py
@Software : PyCharm Community
"""

import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))

# TypeError: Object of type 'Student' is not JSON serializable
# print(json.dumps(s))

