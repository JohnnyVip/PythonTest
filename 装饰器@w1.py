def makeBold(fn):
    #print("----makeBold----")
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeItalic(fn):
    #print("---makeItalic----")
    def wrapped():
        return "<i>" + fn() +"</i>"
    return wrapped

@makeBold
def test1():
    return "hello world-1"

@makeItalic
def test2():
    return "hello world-2"

@makeBold
@makeItalic
def test3():
    return "hello world-3"

test1()
test2()
test3()



