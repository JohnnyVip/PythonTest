#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/23 10:34
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : extend_test.py
@Software : PyCharm Community
"""

class foo(object):
    def __init__(self,driver):
        print('foo __init__ ...')
        self.driver = driver

class child(foo):
    def __init__(self,driver):
         super(child, self).__init__(driver)
    pass

p = child('haha')
