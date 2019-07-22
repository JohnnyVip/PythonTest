# -*- coding:utf-8 -*-

class Game(object):
    #类属性
    num = 0

    #实例方法
    def __init__(self,name):
        #实例属性
        self.name = name

    def get_name(self):
        Game.add_num()
        return self.name

    #类方法
    @classmethod
    def add_num(cls):
        cls.num = 100
    #静态方法
    @staticmethod
    def test_static():
    	return "testStatic"
        

game = Game("laowang")
game.get_name()
Game.add_num()
