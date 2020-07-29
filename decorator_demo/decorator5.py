#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/22 18:33
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : decorator5.py
@Software : PyCharm Community
"""

def NewEat(NewCls):
    class NewEatCls():
        def __init__(self,food,water):
            self.new = NewCls(food)
            self.water = water
        def display(self):
            print('my lunch is ' + self.new.food + ' and ' + self.water)
    return NewEatCls

@NewEat  #Eat = NewEat(Eat)
class Eat(object):
    def __init__(self,food):
        self.food = food
    def display(self):
        print('my lunch is ' + self.food)

if __name__ == "__main__":
    e = Eat('rice','water')
    e.display()
