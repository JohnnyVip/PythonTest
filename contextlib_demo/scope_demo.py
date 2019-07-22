# !/usr/bin/env python3
# -*- coding:utf-8 -*-
num = 10
try:
    num = 1
    num += 2
    print(num)

except Exception as e:
    print(num)


finally:
    print(num)

if num:
    num += 20

def func():
    global num
    #num += 1 #error,定义了一个新的num, local
    print(num)

for i in range(2):
    num += 3

func()

