#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/20 16:07
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : superDemo4.py
@Software : PyCharm Community
"""

# 1.多继承子类对父类构造方法的调用
class Human:
    def __init__(self, sex):
        self.sex = sex

    def p(self):
        print("这是Human的方法")

    def str1(self):
        print("this is" + ' ' + str(self.sex))


class Person:
    def __init__(self, name):
        self.name = name

    def p(self):
        print("这是Person的方法")

    def person(self):
        print("这是我person特有的方法")

    def str2(self):
        print("this is:" + str(self.name))


class Student(Human, Person):  # 注意子类如果没有构造方法时，按括号内父类的继承顺序去继承父类构造方法，只继承一个
    def prin(self):
        print("student")


# ------创建对象 -------------
# stu1=Studnent("男","tom")报错。
stu = Student("sex")  # 这里继承的是Human的构造方法。
stu.p()
stu.str1()
# stu.str2() #报错，因为即使human和person都是一个参数的构造方法，但是这里继承调用的是第一个Human的构造方法
