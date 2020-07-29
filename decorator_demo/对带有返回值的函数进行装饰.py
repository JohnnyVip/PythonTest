def func(functionName):
    print("---func---1---")
    def func_in(*args,**kwargs):
        print("---func_in---1---")
        ret = functionName(*args,**kwargs)
        print("---func_in---2---")
        return ret
    print("---func---2---")
    return func_in

@func
def test1(a):
    print("---test1----")
    return a

@func
def test2(a,b):
    print("---test2----")
    return a,b
@func
def test3(a,b,c):
    print("---test3----")
    return a,b,c

@func
def test4(a,b,c,d):
    print("---test3----")
    return a,b,c,d

def main():
    ret = test4(11,22,33,44)
    print("test return value is %s"%str(ret))


if __name__ == "__main__":
    main()




