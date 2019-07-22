#f1,f2,f3在count执行完的这个背景下（content-text），引用的外部函数局部变量i的值为3

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
