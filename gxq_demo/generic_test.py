#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/16 19:06
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : generic_test.py
@Software : PyCharm Community
"""
from typing import Generic

class R(Generic[T]):
    code: int
    message: str
    result: T

    def __init__(self, r: dict, t: Type[T]):

        self.code = r.get('code')
        self.message = r.get('message')
        if '[' in str(t):
            _c = __class_type__(str(t)[str(t).index('[') + 1:str(t).index(']')])
            self.result = _c(**r.get('result'))
        else:
            self.result = r.get('result')


