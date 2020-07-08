#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/20 16:19
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : superDemo6.py
@Software : PyCharm Community
"""

class Parent(object):
    def __init__(self, name, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束被调用')


class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):
        print('Son1的init开始被调用')
        self.age = age
        super().__init__(name, *args, **kwargs)
        print('Son1的init结束被调用')


class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):
        print('Son2的init开始被调用')
        self.gender = gender
        super().__init__(name, *args, **kwargs)
        print('Son2的init结束被调用')


class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        print('Grandson的init开始被调用')
        # 多继承时，相对于使用类名.__init__方法，要把每个父类全部写一遍
        # 而super只用一句话，执行了全部父类的方法，这也是为何多继承需要全部传参的一个原因
        # super(Grandson, self).__init__(name, age, gender) 效果和下面的一样
        super().__init__(name, age, gender)
        print('Grandson的init结束被调用')


print(Grandson.__mro__)  # 搜索顺序

gs = Grandson('grandson', 12, '男')

print('姓名：', gs.name)
print('年龄：', gs.age)
print('性别：', gs.gender)

'''
执行结果：
(<class '__main__.Grandson'>, <class '__main__.Son1'>, <class '__main__.Son2'>, <class '__main__.Parent'>, <class 'object'>)
Grandson的init开始被调用
Son1的init开始被调用
Son2的init开始被调用
parent的init开始被调用
parent的init结束被调用
Son2的init结束被调用
Son1的init结束被调用
Grandson的init结束被调用
姓名： grandson
年龄： 12
性别： 男
'''

'''
method resolution order:方法解析顺序
'''

'''
注意：在上面模块中，当在子类中通过super调用父类方法时，parent被执行了1次。
super调用过程：上面gs初始化时，先执行grandson中init方法, 其中的init有super调用，
每执行到一次super时，都会从__mro__方法元组中顺序查找搜索。所以先调用son1的init方法，
在son1中又有super调用，这个时候就就根据__mro__表去调用son2的init，然后在son2中又有super调用，
这个就根据mro表又去调用parent中的init，直到调用object中的init.  所以上面的打印结果如此，要仔细分析执行过程。
'''