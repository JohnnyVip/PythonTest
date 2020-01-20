#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/11/12 20:16
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : Gaojiawu.py
@Software : PyCharm Community
"""
api_data = [{'2012': {'kpiValue': '1611178238.37', 'yearOnYear': 0.2655},
             '2032': {'kpiValue': '34233464.16', 'yearOnYear': 0.3477},
             '2031': {'kpiValue': '374739075.03', 'yearOnYear': 0.0158},
             '2030': {'kpiValue': '340505610.87', 'yearOnYear': -0.0088},
             '2007': {'kpiValue': '191536089.34', 'yearOnYear': 0.0853},
             '2029': {'kpiValue': '1419394955.07', 'yearOnYear': -0.0504},
             '2028': {'kpiValue': '3292505556.85', 'yearOnYear': 0.1525},
             '2005': {'kpiValue': '4310934.15', 'yearOnYear': -0.3268},
             '2027': {'kpiValue': '1873110601.78', 'yearOnYear': 0.3752},
             '2004': {'kpiValue': '609775982.13', 'yearOnYear': 0.211},
             '2003': {'kpiValue': '609775982.13', 'yearOnYear': 0.211},
             '2002': {'kpiValue': '2220954220.5', 'yearOnYear': 0.25},
             '5010': {'kpiValue': '1203181000', 'yearOnYear': 0.3398}}]
# 'reportDate': 1569772800000,
def func():
    new_api_data = []
    _keys0 = api_data[0].keys()
    for s0 in _keys0:
        new_api_data0 = []
        _keys1 = api_data[0].get(s0).keys()
        for s1 in _keys1:
            new_api_data0.append(api_data[0].get(s0).get(s1))
        new_api_data.append(s0)
        new_api_data.append(new_api_data0)
    return  new_api_data

# print(func())

a = {"name":"yaoqiang","age":23,"sex":0}
print(a.get("name"))




