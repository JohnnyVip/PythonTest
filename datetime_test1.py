#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/9/6 13:27
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : datetime_test1.py
@Software : PyCharm Community
"""
import datetime

_today = datetime.datetime.today()
# Note:默认的起始日期 = 结束日期 - 6天
default_date = _today - datetime.timedelta(days=6)
day_times = default_date.day
print(day_times)
print(type(day_times))

