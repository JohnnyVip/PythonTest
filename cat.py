# -*- coding:utf-8 -*-

class Animal(object):
    def __init__(self,name):
        self.name = name
        #print(id(self))
        
class Cat(Animal):
    def __init__(self,name,age):
        #Animal.__init__(self,name)
        #super().__init__(name)
        super(Cat,self).__init__(name)
        self.age = age
        #print(id(self))

    def __str__(self):
        return self.name + ":" + self.age

cat = Cat("tom","30")

def main(Animal):
    print(Animal)

main(cat)

        

