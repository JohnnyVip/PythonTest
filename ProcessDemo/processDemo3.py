#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/23 14:08
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : processDemo3.py
@Software : PyCharm Community
"""

import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)