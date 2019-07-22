# !/usr/bin/env python3
# -*- coding:utf-8 -*-
#错误示例
try:
    f = open('/path/to/file', 'r')
    f.read()
finally:
    if f:
        f.close()

