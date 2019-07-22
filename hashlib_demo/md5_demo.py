# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import hashlib

md5 = hashlib.md5()
md5.update('123456'.encode('utf-8'))
print(md5.hexdigest())


md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())