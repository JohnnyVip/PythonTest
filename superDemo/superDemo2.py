#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/20 14:51
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : superDemo2.py
@Software : PyCharm Community
"""

class land(object):
    def me(self):
        print('land')

    def run(self):
        print('run...')

class sky(object):
    def me(self):
        print('fly')

    def fly(self):
        print('fly...')

# class plane(land, sky):
#     pass


class plane(land, sky):
    def me(self):
        super().me()  # land的me
        super(plane, self).me()  # land的me
        super(land, self).me()  # sky的me

p = plane()

p.me()


# p = plane()
#
# p.run()
# p.fly()
# p.me()