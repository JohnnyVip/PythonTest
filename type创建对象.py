#coding=utf-8

def printNum(self):
    print("---num-%d"%self.num)
    
Test = type("Test3",(),{"printNum":printNum})

Test.__class__


#1874819648
#>>> id(b)
#1874819648
