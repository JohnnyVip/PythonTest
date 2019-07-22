# -*- coding:utf-8 -*-

class Tool(object):
    #类属性
    num = 0
    def __init__(self,name):
        self.name = name
        self.num = 88
        Tool.num += 1
        
tool1 = Tool("铁锹")
tool2 = Tool("工兵铲")
tool3 = Tool("水桶")
#delattr(tool1,'num')
#del tool1.num
#del Tool.num

print(Tool.num)

        

