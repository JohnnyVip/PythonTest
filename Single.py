# -*- coding:utf-8 -*-

class Single(object):
	#类属性，私有属性，保存单例引用
	__single = None
	__init_flag = False

	#创建对象
	def __new__(cls,name):
		if not Single.__single:
			Single.__single = object.__new__(cls)
			return Single.__single
		else:
			return Single.__single

	#初始化对象
	def __init__(self,name):
		if not Single.__init_flag:
			Single.__init_flag = True
			self.name = name
		
single1 = Single("single1")
print("id(single1) = %d,name is %s"%(id(single1),single1.name))
single2 = Single("single2")
print("id(single2) = %d,name is %s"%(id(single2),single2.name))
single3 = Single("single3")
print("id(single3) = %d,name is %s"%(id(single3),single3.name))