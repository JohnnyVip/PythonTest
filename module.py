# -*- coding:utf-8 -*-

__all__ = ["HelloWorld","test1"]

import time

class HelloWorld(object):
	def hello_world(self):
		print("hello world")

def test1():
	print("-----test1-------")

def test2():
	print("------test2------")

num = 10

def main():
	print("num is %d"%num)
	test1()
	test2()
	HelloWorld().hello_world()

if __name__ == '__main__':
	main()
