#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/6/16 15:19
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : get_html.py
@Software : PyCharm Community
"""

import urllib.request

def gethtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

html = gethtml("https://www.baidu.com/")

print (html)
