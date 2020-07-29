#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/22 17:28
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : IODemo2.py
@Software : PyCharm Community
"""

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

