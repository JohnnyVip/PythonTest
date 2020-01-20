#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/12/16 20:28
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : re_demo.py
@Software : PyCharm Community
"""
import re

data = ['2019-09-30', '2019-06-30', '2019-03-31',
        '2018-12-31', '2018-09-30', '2018-06-30',
        '2018-03-31', '2017-12-31', '2017-09-30',
        '2017-06-30', '2017-03-31', '2016-12-31',
        '2016-09-30', '2016-06-30', '2016-03-31',
        '2015-12-31', '2015-09-30', '2015-06-30',
        '2015-03-31', '2014-12-31']
date_list=[]
for i in data:
    date_all = re.findall("\d{4}-09-30",i)
    if date_all != []:
        date_list += date_all
print(date_list)

