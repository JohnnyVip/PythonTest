#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/23 14:52
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : logger_demo3.py
@Software : PyCharm Community
"""

#import logging
import logging.handlers

logger = logging.getLogger("logger")
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.debug('This is a customer debug message')
logger.info('This is an customer info message')
#极易犯错误的地方
logging.warning('This is a customer warning message')
logger.error('This is an customer error message')
logger.critical('This is a customer critical message')

