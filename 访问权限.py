# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
    import Module              # 引入模块
    from Module import Other  # 引入模块中的类、函数或者变量
    from Module import *       # 引入模块中的所有‘公开’成员

    其区别就是:
    第一个：引入的模块(假如是 mdemo )会自动生成一个‘对象‘以模块名命名，然后就可以通过这个‘对象’(mdemo)获取该模块里面的类、函数或变量等
    第二个：引入模块中的Other(这里的Other就是模块中定义的成员)成员，调用时就可以省略 模块名。
    第三个：这种情况如果上面的第二个弄懂的话就不难理解了,其意思就是引入模块中所有'公开'的成员。

'''

from hello import *

test()
#print(_a)
#print(__a)

import datetime

print(datetime.datetime.now())