#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/22 13:27
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : propertyDemo2.py
@Software : PyCharm Community
"""

class Screen(object):

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,width_value):
        self.__width = width_value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,height_value):
        self.__height=height_value

    @property
    def resolution(self):
        return self.width * self.height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')