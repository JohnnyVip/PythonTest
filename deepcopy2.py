import copy


class A(object):
    def __init__(self):
        print('__init__被执行了！')


class B(object):
    def __init__(self):
        self.a = A()


b = B()
#c = copy.copy(b)
d = copy.deepcopy(b) #b指向的对象被重新copy了一份