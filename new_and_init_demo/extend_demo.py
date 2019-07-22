#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Person(object):
    def __init__(self,name,sex,weight):
        print(id(self))
        self.name = name
        print(id(self.name))
        self.sex = sex
        print(id(self.sex))
        self.__weight = weight
        print(id(self.__weight))

class Child(Person):                          # Child 继承 Person
    #调用父类的__init__方法创建的属性，都归属于父类(name,sex,__weight)
    def __init__(self,name,sex,weight,mother,father):
        Person.__init__(self,name,sex,weight)  # Person类对象引用不会传递给self,子类对父类的构造方法的调用,这里的self是Child的实例化对象的引用
        self.mother = mother
        self.father = father

    #该方法访问不到父类属性__weight
    def show(self):
        print(self.__weight)

May = Child("May","female","April","June",80)
print(May.name,May.sex,May.mother,May.father)
#May.show()
print(id(May.name))
print(id(May.sex))
print(id(May))
