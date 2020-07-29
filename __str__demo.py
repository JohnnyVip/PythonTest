#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/7/21 14:19
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : __str__demo.py
@Software : PyCharm Community
"""

'''
这样便是init最普通的用法了。但init其实不是实例化一个类的时候第一个被调用的方法。
当使用 Persion(name, age) 这样的表达式来实例化一个类时，最先被调用的方法 其实是 new 方法。
'''

class Person(object):
    """Silly Person"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '<Person: %s(%s)>' % (self.name, self.age)


if __name__ == '__main__':
    piglei = Person('piglei', 24)
    print(piglei)