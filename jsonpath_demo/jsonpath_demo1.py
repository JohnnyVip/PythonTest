#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/6/3 18:14
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : jsonpath_demo1.py
@Software : PyCharm Community
"""

d={
        "error_code": 0,
        "stu_info": [
                {
                        "id": 2059,
                        "name": "小白",
                        "sex": "男",
                        "age": 28,
                        "addr": "河南省济源市北海大道32号",
                        "grade": "天蝎座",
                        "phone": "18378309272",
                        "gold": 10896,
                        "info":{
                            "card":434345432,
                            "bank_name":'中国银行'
                        }

                },
                {
                        "id": 2067,
                        "name": "小黑",
                        "sex": "男",
                        "age": 28,
                        "addr": "河南省济源市北海大道32号",
                        "grade": "天蝎座",
                        "phone": "12345678915",
                        "gold": 100
                }
        ]
}

res= d["stu_info"][1]['name'] #取某个学生姓名的原始方法:通过查找字典中的key以及list方法中的下标索引
print(res) #输出结果是：小黑

import jsonpath
res1=jsonpath.jsonpath(d,'$..name') #嵌套n层也能取到所有学生姓名信息,$表示最外层的{}，..表示模糊匹配
print(res1) #输出结果是list：['小白', '小黑']

res2= jsonpath.jsonpath(d,'$..bank_name')
print(res2) #输出结果是list：['中国银行']

res3=jsonpath.jsonpath(d,'$..name123') #当传入不存在的key(name)时,返回False
print(res3) #输出结果是：False