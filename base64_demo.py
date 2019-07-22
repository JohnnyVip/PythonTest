# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import base64

def print_hex(_bytes):
    l = [hex(int(i)) for i in _bytes]
    print(" ".join(l))

encodestr = base64.b64encode(b'binary\x00string')

print_hex(encodestr)

print(int('010110',2))
print(chr(int('010110',2)))

print('binary\x00string')
print(encodestr)

