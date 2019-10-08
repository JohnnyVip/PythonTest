#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/23 14:04
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : logger_demo.py
@Software : PyCharm Community
"""

import logging
#import logging.handlers

logger = logging.getLogger(__name__)

def log_func():
    '''
    测试logger
    :return:
    '''
    handler1 = logging.StreamHandler() #控制台
    handler2 = logging.FileHandler(filename="test.log", encoding="utf-8") #日志存储目录

    logger.setLevel(logging.DEBUG)
    handler1.setLevel(logging.WARNING)
    handler2.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
    handler1.setFormatter(formatter)
    handler2.setFormatter(formatter)

    logger.addHandler(handler1)
    logger.addHandler(handler2)

    # 分别为 10、30、30
    # print(handler1.level)
    # print(handler2.level)
    # print(logger.level)

    logger.debug('This is a customer debug message')
    logger.info('This is an customer info message')
    logger.warning('This is a customer warning message')
    logger.error('This is an customer error message')
    logger.critical('This is a customer critical message')

if __name__ == '__main__':
    log_func()