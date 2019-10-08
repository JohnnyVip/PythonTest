def func(functionName):
    print("---func---1---")
    def func_in():
        print("---func_in---1---")
        functionName()
        print("---func_in---2---")

    print("---func---2---")
    return func_in

@func #test = func(test)
def test():
    print("---test----")
    return "haha"

ret = test()
print("test return value is %s"%ret)
    

