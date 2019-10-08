#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/8/5 14:48
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : date_demo.py
@Software : PyCharm Community
"""
import datetime

_today = datetime.date.today()

print(type(_today))

print(_today)

_today = datetime.date.today().strftime("%Y%m%d")

print(type(_today))

print(_today)
#
# _today = datetime.datetime.strptime(str(_today), '%Y-%m-%d')
#
# print(_today)
# print(type(_today))

# _init_date = datetime.datetime.strptime(str(20170312), '%Y%m%d')
#
# print(_init_date)
#
# print(type(_init_date))
#
# print(_init_date.year)
# print(_init_date.month)
# print(_init_date.day)
#
# year_times = _init_date.year - _today.year
# month_times = _init_date.month - _today.month
# day_times = _init_date.day - _today.day
# print(year_times,month_times,day_times)
#
#
# print("=================================")
# # for i in range(abs(month_times)):
# #     print(i)
#
# # for i in range(abs(month_times)):
# #     print(i)
#
# for i in range(-1):
#     print(i)