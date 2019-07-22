#coding=utf-8

def count():
    #闭包，外层函数是f,内层函数是g,返回的是内层函数的地址。外层变量i和g构成闭包
    #函数要在调用之前定义
    #-------------------
    def f(i):
        def g():
            return i*i
        return g
    #-------------------     
    fs = []
    for i in range(1,4):      
        fs.append(f(i))#将外层函数f的返回值存贮到列表fs中
    return fs

f1,f2,f3 = count()
