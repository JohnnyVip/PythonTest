#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/23 14:29
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : logger_demo1.py
@Software : PyCharm Community
"""

import logging

logging.basicConfig(filename="test.log", filemode="w", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)
a = 5
b = 0
try:
    c = a / b
except Exception as e:
    # 下面三种方式三选一，推荐使用第一种
    logging.exception("Exception occurred")
    #logging.info('start exception...')
    #logging.error("Exception occurred", exc_info=True)
    #logging.log(level=logging.DEBUG, msg="Exception occurred", exc_info=True)

