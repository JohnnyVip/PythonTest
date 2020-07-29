#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/7/24 15:06
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : logger_demo.py
@Software : PyCharm Community
"""

import logging
import os
import time
class Logger:
    def __init__(self,level="DEBUG",log_name=time.strftime("%Y-%m-%d.log", time.localtime()),
                 log_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "log"),use_console=True):
        logger = logging.getLogger(__name__)
        logger.setLevel(level)
        formatter = logging.Formatter("%(funcName)s-%(asctime)s - %(name)s -%(levelname)s - %(message)s")
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        handler_list = list()
        handler_list.append(logging.FileHandler(os.path.join(log_path, log_name), encoding="utf-8"))
        if use_console:
            handler_list.append(logging.StreamHandler())
        for handler in handler_list:
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        self.logger = logger

    #def debug(self,msg):
     #   return self.logger.debug(msg)
    #def critical(self,msg):
     #   return self.logger.critical(msg)
    def __getattr__(self, item):
        return getattr(self.logger,item)

#if __name__ == "__main__":

 #   x = Logger()