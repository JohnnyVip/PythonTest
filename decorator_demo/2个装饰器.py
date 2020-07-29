def w1(func):
    print("---正在装饰1----")
    def inner2():
        print("---正在验证权限1---")
        func()
    return inner2

def w2(func):
    print("---正在装饰2---- ")
    def inner1():
        print("---正在验证权限2----")
        func()
    return inner1

#只要python解释器执行到了这个代码，那么就会自动的进行装饰，而不是等到调用的时候在装饰
@w1 # f1 = w1(f1=inner1) -> inner2
@w2 #f1 = w2(f1) -> inner1
def f1(): # f1 = w1(w2(f1))
    print("----f1----")

#在调用f1之前，已经完成装饰了
f1()
    

