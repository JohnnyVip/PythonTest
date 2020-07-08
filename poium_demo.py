#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/6/1 19:23
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : poium_demo.py
@Software : PyCharm Community
"""
from poium import Page, NewPageElement
from selenium import webdriver


class BaiduIndexPage(Page):
    search_input = NewPageElement(name='wd')
    search_button = NewPageElement(id_='su')


driver = webdriver.Chrome()

page = BaiduIndexPage(driver)
page.get("https://www.baidu.com")

page.search_input = "poium"
page.search_button.click()

driver.quit()

