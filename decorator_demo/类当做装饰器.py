class Test(object):
    def __init__(self,func):
        print("---初始化---")
        print("func name is %s"%func.__name__)
        self.__func = func

    def __call__(self):
        print("---装饰器中的功能---")
        self.__func()

@Test
def test(): # test = Test(test)
    print("---test----")

test()#test是Test的一个对象，test()调用__call__方法
