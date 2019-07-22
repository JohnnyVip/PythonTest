#模块的来源
'''
1. 系统提供的
2. 第三方的
3. 自己定义的
'''

#导入模块的方式
'''
1. import xxx
2. from xxx import xxx1,xxx2 
3. rom xxx import *
4. import xxx as it 起别名

注意：
1. 2,3的导入方式，有可能造成方法掩盖，例如，xxx1和xxx2均有test方法，
   此时xxx1的test将被掩盖
2. 模块默认首先从当前路径导入，找不到时再去安装目录: D:\Python36\Lib
'''

import XXX

__all__ = ["ClassName","function"]

class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg

num = 100,#导入模块的时候访问不到，因为__all__列表中没有num，限制了num的访问		

def function():
	pass


def main():
	pass

'''
注意：
1.直接运行模块的函数 如python xxx(),此时__name__ = __main__
2.由其它导入模块xxx.py,此时__name__ = xxx
3.__all__ = []
'''
if __name__ == '__main__':
	main()