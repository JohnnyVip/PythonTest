#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/16 9:51
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : keyevent_test.py
@Software : PyCharm Community
"""
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = '9f348b37'
desired_caps['appPackage'] = 'com.android.contacts'
desired_caps['appActivity'] = 'com.android.contacts.activities.TwelveKeyDialer'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.find_element_by_class_name("android.widget.LinearLayout").click()

driver.find_element_by_id("android:id/icon").click()

name = driver.find_element_by_android_uiautomator('new UiSelector().text("姓名")')
name.send_keys('test')

phone = driver.find_element_by_android_uiautomator('new UiSelector().text("电话")')
phone.send_keys('13800138000')

driver.find_element_by_android_uiautomator('new UiSelector().text("确认")').click()

driver.quit()

