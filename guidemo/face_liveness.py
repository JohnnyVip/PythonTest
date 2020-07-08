#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/7/3 13:46
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : face_liveness.py
@Software : PyCharm Community
"""
import base64

from aip import AipFace


def get_face_liveness():

    """ clock_in_class """
    APP_ID = '20687731'
    API_KEY = 'pXuzuyEU0tnjwpKmNBpFaNQc'
    SECRET_KEY = 'VRfVVGtlSpl1Z0UhuRgQSzvCvNSSmW7A'

    # 客户信息
    client = AipFace(APP_ID, API_KEY, SECRET_KEY)

    result = client.faceverify([
        {
            'image': bytes.decode(base64.b64encode(open('save.jpg', 'rb').read())),
            'image_type': 'BASE64',
        }
    ])

    return result

if __name__ == '__main__':
    print(get_face_liveness())