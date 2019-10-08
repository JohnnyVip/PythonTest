#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/8/13 15:09
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : deleteZero.py
@Software : PyCharm Community
"""

def deleteZero(num:str=None):
    '''
    0.81568000
    若一个8位小数的最低3位是0，则将其删除，低4位小数无论是否为0,均保留!
    :param num:
    :return:
    '''
    length = len(num)

    reverse_num = num[::-1]

    cnt = 0

    for ch in reverse_num:
        if ch == '0':
            cnt += 1
            if cnt == 3:
                break
        else:
            break

    num = num[0:length-cnt]

    return num

print(deleteZero('0.81568000'))
print(deleteZero('0.81568001'))
print(deleteZero('0.81560000'))

