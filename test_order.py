#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/12/27 9:55
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : test_order.py
@Software : PyCharm Community
"""
import pytest


class TestOrder:
    """测试order"""

    @pytest.mark.order(1*2)
    def test_01_func(self):
        print("=========test01============")
        pass

    @pytest.mark.order(1*1+6)
    def test_02_func(self):
        print("=========test02============")
        pass

    @pytest.mark.order(0)
    def test_03_func(self):
        print("=========test03============")
        pass
