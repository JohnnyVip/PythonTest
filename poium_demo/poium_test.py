#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/6/1 19:06
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : poium_test.py
@Software : PyCharm Community
"""

from poium import Page, PageElement
from selenium import webdriver

class LoginPage(Page):
    username = PageElement(name='user_name')
    password = PageElement(name='password')
    login_button = PageElement(id_='startlogin')

driver = webdriver.Chrome()
page = LoginPage(driver)
page.get("http://192.168.61.127/yjbadmin-web/user/login")
page.username.send_keys("姚强")
page.password.send_keys("@gjzq20200415")
page.login_button.click()

