# -*- coding:utf-8 -*-

class Animal(object):
    def __init__(self,name):
        self.name = name
        print("父类构造方法被执行了")
    def __str__(self):
        return self.name
        
class Dog(Animal):
    pass

cat = Dog("hashchi")

def main(Animal):
    print(Animal)

main(cat)

        

