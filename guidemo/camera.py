#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/7/2 17:57
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : camera.py
@Software : PyCharm Community
"""

from tkinter import *
import cv2 as cv
from PIL import Image, ImageTk
import os

workpath = os.path.dirname(sys.argv[0])
os.chdir(workpath)  # 指定py文件执行路径为当前工作路径

# 临时变量
tempimagepath = r"./yaoqiang_18516730037.jpg"

# 摄像机设置
# 0是代表摄像头编号，只有一个的话默认为0
capture = cv.VideoCapture(0)


def getframe():
    ref, frame = capture.read()
    cv.imwrite(tempimagepath, frame)


def closecamera():
    capture.release()

# 界面相关
window_width = 640
window_height = 480
image_width = int(window_width * 0.6)
image_height = int(window_height * 0.6)
imagepos_x = int(window_width * 0.2)
imagepos_y = int(window_height * 0.1)
butpos_x = 250
butpos_y = 350

top = Tk()
top.wm_title("face recognition")
top.geometry(str(window_width) + 'x' + str(window_height))


def tkImage():
    ref, frame = capture.read()
    cvimage = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
    pilImage = Image.fromarray(cvimage)
    pilImage = pilImage.resize((image_width, image_height), Image.ANTIALIAS)
    tkImage = ImageTk.PhotoImage(image=pilImage)
    return tkImage


def button1():
    ref, frame = capture.read()
    cv.imwrite(tempimagepath, frame)


# 控件定义
canvas = Canvas(top, bg='white', width=image_width, height=image_height)  # 绘制画布
b = Button(top, text='savepicture', width=15, height=2, command=button1)

# 控件位置设置
canvas.place(x=imagepos_x, y=imagepos_y)
b.place(x=butpos_x, y=butpos_y)

if __name__ == "__main__":
    while True:
        picture = tkImage()
        canvas.create_image(0, 0, anchor='nw', image=picture)
        top.update()
        top.after(100)

    # top.mainloop()
    # closecamera()