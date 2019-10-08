#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/24 19:59
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : property_test1.py
@Software : PyCharm Community
"""

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

#error
#s = Student().score()

s = Student().score

print(s)
