# !/usr/bin/env python3
# -*- coding:utf-8 -*-

from functools import reduce

def str2float(s):

    def char2num(s):
        DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return DIGITS[s]

    def fni(x, y):
        return x * 10 + y

    def fnf(x, y):
        return x * 0.1 + y

    # def strReverse(strDemo):
    #     strList = list(strDemo)
    #     strList.reverse()
    #     return ''.join(strList)


    return reduce(fni, map(char2num,s.split('.')[0])) + 0.1*reduce(fnf, map(char2num,s.split('.')[1][::-1]))

print(str2float('123.456'))

