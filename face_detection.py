#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/7/1 15:30
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : face_detection.py
@Software : PyCharm Community
"""
import base64
import time

import cv2
from aip import AipFace

# #调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
# cap=cv2.VideoCapture(0)
# while True:
#     #从摄像头读取图片
#     sucess,img=cap.read()
#
#     #显示摄像头
#     cv2.imshow("vedio",img)
#
#     #保持画面的持续。
#     k=cv2.waitKey(1)
#
#     if k == 27:
#         #通过esc键退出摄像
#         cv2.destroyAllWindows()
#         break
#     elif k==ord("s"):
#         #通过s键保存图片，并退出。
#         cv2.imwrite("image2.jpg",img)
#         cv2.destroyAllWindows()
#         break
# #关闭摄像头
# cap.release()


""" clock_in_class """
APP_ID = '20687731'
API_KEY = 'pXuzuyEU0tnjwpKmNBpFaNQc'
SECRET_KEY = 'VRfVVGtlSpl1Z0UhuRgQSzvCvNSSmW7A'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


result = client.match([
    {
        'image': bytes.decode(base64.b64encode(open('image.jpg', 'rb').read())),
        'image_type': 'BASE64',
        "face_type": "LIVE",
        "liveness_control": "NONE"
    },
    {
        'image': bytes.decode(base64.b64encode(open('Haitong.jpg', 'rb').read())),
        'image_type': 'BASE64',
        "face_type": "LIVE",
        "liveness_control": "NONE"
    }
])

print(result)