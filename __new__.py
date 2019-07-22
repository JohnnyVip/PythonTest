# -*- coding:utf-8 -*-

class Dog:
    def __init__(self):
        #print(id(self))
        print("-----init方法-------")
    def __del__(self):
        print("-----del方法-------")
    def __str__(self):
        print("-----strt方法-------")
    def __new__(cls):
        print("----new方法----")
        d = object.__new__(cls)
        #print(id(d))
        return d

dog1 = Dog()
dog2 = Dog()

