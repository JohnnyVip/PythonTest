# !/usr/bin/env python3
# -*- coding:utf-8 -*-

def print_hex(_bytes):
    l = [hex(int(i)) for i in _bytes]
    print(" ".join(l))

b = b"Hello, world!"  # bytes object
s = "Hello, world!"   # str object

print_hex(b)

print('str --> bytes')
print(bytes(s, encoding="utf8"))
print(str.encode(s))   # 默认 encoding="utf-8"
print(s.encode())      # 默认 encoding="utf-8"

print('\nbytes --> str')
print(str(b, encoding="utf-8"))
print(bytes.decode(b))  # 默认 encoding="utf-8"
print(b.decode())       # 默认 encoding="utf-8"


