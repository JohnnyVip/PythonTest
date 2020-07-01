#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/5/26 14:51
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : ugly_number.py
@Software : PyCharm Community
"""

"""
请你帮忙设计一个程序，用来找出第 n 个丑数。
丑数是可以被 a 或 b 或 c 整除的 正整数

示例 1：

输入：n = 3, a = 2, b = 3, c = 5
输出：4
解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。

示例 2：
输入：n = 4, a = 2, b = 3, c = 4
输出：6
解释：丑数序列为 2, 3, 4, 6, 8, 9, 12... 其中第 4 个是 6。

示例 3：
输入：n = 5, a = 2, b = 11, c = 13
输出：10
解释：丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。

示例 4：
输入：n = 1000000000, a = 2, b = 217983653, c = 336916467
输出：1999999984
 
提示：
1 <= n, a, b, c <= 10^9
1 <= a * b * c <= 10^18
本题结果在 [1, 2 * 10^9] 的范围内

"""

def ugly_number_query(n:int,a:int,b:int,c:int)->int:
    """
    :param n: 第n个丑数
    :param a:
    :param b:
    :param c:
    :return:
    """
    # 计数
    cnt = 0

    # 基数
    num = min(a, b, c)

    while True:

        if (not num % a) or (not num % b) or (not num % c):

            cnt += 1

            if cnt == n:
                break

            num += 1

            continue

        else:

            num += 1

    return num

if __name__ == '__main__':
    print(ugly_number_query(3,2,3,5))
    print(ugly_number_query(4,2,3,4))
    print(ugly_number_query(5,2,11,13))
    print(ugly_number_query(1000000000,2,217983653,336916467))