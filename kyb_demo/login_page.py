#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/15 14:18
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : login_page.py
@Software : PyCharm Community
"""
from time import sleep

from appium import webdriver

UserName = 'zxw1234'
Pwd = 'zxw123456'

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = '9f348b37'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.close_app()

driver.find_element_by_id('android:id/button2').click()
sleep(2)

#driver.find_element_by_id('android:id/button2').click()
#driver.find_element_by_name('取消').click()
driver.find_element_by_android_uiautomator('new UiSelector().text("取消")').click()
#driver.find_elements_by_class_name('android.widget.Button')[0].click()
sleep(2)

driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()
sleep(2)

username = driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']")
username.clear()
username.send_keys(UserName)
sleep(2)

pwd = driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext')
pwd.clear()
pwd.send_keys(Pwd)
sleep(2)

driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()
sleep(5)

driver.quit()

def find_element_by_name(text):
    pass