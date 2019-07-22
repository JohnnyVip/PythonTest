#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
如果重写了__init__ 时，要继承父类的构造方法，可以使用 super 关键字：
super(子类，self).__init__(参数1，参数2，....)

还有一种经典写法：
父类名称.__init__(self,参数1，参数2，...)

'''

class Father(object):
    def __init__(self, name):
        self.name = name
        print ("name: %s" % (self.name))

    def getName(self):
        return 'Father ' + self.name


class Son(Father):
    def __init__(self, name):
        super(Son, self).__init__(name)
        print ("hi")
        self.name = name

    def getName(self):
        #print(super(Son,self).getName())
        print(Father.getName(self))
        return 'Son ' + self.name


if __name__ == '__main__':
    son = Son('runoob')
    print (son.getName())