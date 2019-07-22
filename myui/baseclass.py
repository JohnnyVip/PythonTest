#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/12 13:29
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : baseclass.py
@Software : PyCharm Community
"""

from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = '9f348b37'
desired_caps['appPackage'] = 'com.miui.calculator'
desired_caps['appActivity'] = '.cal.CalculatorActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# driver.find_element_by_id("com.miui.calculator:id/btn_2_s").click()
# driver.find_element_by_id("com.miui.calculator:id/btn_0_s").click()
# driver.find_element_by_id("com.miui.calculator:id/btn_1_s").click()
# driver.find_element_by_id("com.miui.calculator:id/btn_9_s").click()
# driver.find_element_by_id("com.miui.calculator:id/btn_plus_s").click()
# driver.find_element_by_id("com.miui.calculator:id/btn_1_s").click()
# driver.find_element_by_id("com.miui.calculator:id/btn_equal_s").click()
sleep(5)
driver.quit()
