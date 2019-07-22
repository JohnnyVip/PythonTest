#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# def fib_yield(n):
#     a, b = 0, 1
#     while b < n:
#         yield b
#         a, b = b, a+b

'''
这是一个fibonacci模块
可以观察到，fibonacci.py 在作为模块引入时，fibonacci.__name__ 被设置为文件名 "fibonacci"。
但若在命令行直接执行 python fibonacci.py，则 if 语句块会被执行，此时 __name__ 是 "__main__"。
'''

#前n个fibonacci数的generator
def fib_yield(n):
    cnt = 0
    a, b = 0, 1
    while True:
        yield b
        cnt += 1
        if cnt == n:
            break
        a, b = b, a+b

def fib(n):
    for num in fib_yield(n):
        print(num)

if __name__ == "__main__":
    fib(10)