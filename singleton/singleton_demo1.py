#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/7/23 11:06
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : singleton_demo1.py
@Software : PyCharm Community
"""


def singleton(cls):
    """
    单例装饰器
    :param cls:
    :return:
    """
    instance = {}

    def get_instance(*args,**kwargs):
        if cls not in instance:
            instance[cls] = cls(*args,**kwargs)
        return instance[cls]
    return get_instance


# Student = singleton(Student)
@singleton
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student('qiang',25)
student2 = Student('cheng',25)
print(student1)
print(student2)
print(student1==student2)
