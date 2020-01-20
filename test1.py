#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/10/10 15:20
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : test1.py
@Software : PyCharm Community
"""
a = '20191009'

def timeFormatting(t):
    t1 = t[0:4]+'-'+t[4:6]+'-'+t[6:]
    return t1

print(timeFormatting(a))


class A():
    def run(self):
        A.static_run()
        print("run------------")

    @staticmethod
    def static_run():
        print("run 被调用了----------")
        pass

A().run()