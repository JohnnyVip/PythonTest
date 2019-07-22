# !/usr/bin/env python3
# -*- coding:utf-8 -*-

class Demo():
    def method(self,*args):
        return sum(args)

    def show(self):
        print("show run ...")

    @classmethod
    def static_method(cls):
        print('static_method run...')



