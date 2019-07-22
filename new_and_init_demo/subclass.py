#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Person(object):
    pass

class Child(Person):                 # Child 继承 Person
    pass

May = Child()
Peter = Person()

print(isinstance(May,Child))         # True
print(isinstance(May,Person))        # True
print(isinstance(Peter,Child))       # False
print(isinstance(Peter,Person))      # True
print(issubclass(Child,Person))      # True