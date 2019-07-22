#!/usr/bin/python3

# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w #这个属性只有父类有，子类无法继承

    def speak(self):
        print("%s 说: 我 %d 岁,我 %d斤。" % (self.name, self.age,self.__weight))


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # # 覆写父类的方法
    # def speak(self):
    #     print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))
    #     print("%s 说: 我 %d 岁了，我在读 %d 年级,我的体重是 %d 斤" % (self.name, self.age, self.grade，self.__weight)) #error

s = student('ken', 10, 60, 3)
s.speak()