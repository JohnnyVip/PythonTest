#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/6/16 18:03
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : get_id_1_to_6.py
@Software : PyCharm Community
"""

from poium import Page, PageElement
from selenium import webdriver

province_id = ["北京市","天津市","上海市","重庆市","河北省","内蒙古",
               "山西省","福建省","江西省","山东省","浙江省","江苏省",
               "安徽省","海南省","广西","广东省","湖南省","湖北省",
               "河南省","辽宁省","吉林省","黑龙江省","新疆","青海省",
               "宁夏","甘肃省","陕西省","西藏","贵州省","云南省","四川省",
               "香港","澳门","台湾"]
index =  range(1, len(province_id)+1)

class LoginPage(Page):
    province_name = PageElement(xpath=f'/html/body/main/article/div[2]/div/p/a[{index[11]}]')
    city_name = PageElement(name='password')
    login_button = PageElement(id_='startlogin')

driver = webdriver.Chrome()
page = LoginPage(driver)
page.get("https://bajiu.cn/sfz/?id=1")
page.province_name.send_keys("姚强")
page.password.send_keys("@gjzq20200415")
page.login_button.click()