class Test(object):
    def __init__(self):
        self.__age = 66
        
    @property
    def age(self):
        print("------getter-----")
        return self.__age
    
    @age.setter
    def age(self,newAge):
        print("------setter-----")
        if newAge > 100 or newAge < 0:
            print("设置有误，请重新输入")
            return
        self.__age = newAge
        
t = Test()

t.age = 101

print(t.age)
