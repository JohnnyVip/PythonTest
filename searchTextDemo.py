#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/11/7 17:07
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : searchTextDemo.py
@Software : PyCharm Community
"""

import os

def readFilename(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files, dirs, root

def findstring(pathfile):
    fp = open(pathfile, "r", encoding='UTF-8')  # 注意这里的打开文件编码方式
    strr = fp.read()
    if (strr.find("trimQuotation") != -1):
        print('here?')
        return True
    return False

def startfind(files, dirs, root):
    for ii in files:
        # print(ii)
        # if ii.endswith('.lua'):
        try:
            if (findstring(root + "\\" + ii)):
                print(ii)
        except Exception as err:
            print(err)
            continue

    for jj in dirs:
        fi, di, ro = readFilename(root + "\\" + jj)
        startfind(fi, di, ro)

if __name__ == '__main__':
    default_dir = u"E:\\反洗钱测试复习资料"  # 设置默认打开目录
    file_path = default_dir  # th.expanduser(default_dir)))
    files, dirs, root = readFilename(file_path)
    startfind(files, dirs, root)



