#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/6/16 17:09
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : crack_id_number.py
@Software : PyCharm Community
"""

from poium import Page, PageElement
from selenium import webdriver

class LoginPage(Page):
    name = PageElement(id_='txtName')
    school = PageElement(id_='txtSchool')
    query = PageElement(xpath='//*[@id="form2"]/input[3]')

driver = webdriver.Chrome()
page = LoginPage(driver)
page.get("http://www.hzhr.com/Web/Agent/Archives.html%EF%BC%88%E6%B9%96%E5%B7%9E%E4%BA%BA%E6%89%8D%E7%BD%91%EF%BC%89")
page.name.send_keys("郁乐乐")
page.school.send_keys("浙江大学")
page.query.click()
