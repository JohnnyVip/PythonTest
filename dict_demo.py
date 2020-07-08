#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/6/8 11:15
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : dict_demo.py
@Software : PyCharm Community
"""

a = {"a":123}
print(a.keys())

syl_total_id_api = 1
syl_year_id_api = 2
syl_month_id_api = 3

syl_month_id_db_1 = 4
syl_month_id_db_2 = 5
syl_month_id_db_3 = 6

if syl_month_id_db_1 in [syl_total_id_api,syl_year_id_api]:
    if syl_month_id_db_2 in [syl_total_id_api,syl_year_id_api]:
        syl_month_id_db = syl_month_id_db_3
    else:
        syl_month_id_db = syl_month_id_db_2
else:
    syl_month_id_db = syl_month_id_db_1

# 断言
assert syl_month_id_db == syl_month_id_api
pass


