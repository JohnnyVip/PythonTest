# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import hashlib
'''SHA1:Secure Hash Algorithm'''
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
