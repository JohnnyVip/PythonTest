#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/12 13:43
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : page_login.py
@Software : PyCharm Community
"""

import logging
import os
import glob
import unittest
from time import sleep
import time
import sys
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

YOUR_QQ = '1445524029'
YOUR_PASSWORD = 'qiang,2877'

PLATFORM_VERSION = '6.0.1'

class Wechat():

    def __int__(self):

        app = os.path.abspath(
                os.path.join(os.path.dirname(__file__),
                             'weixin705android1440.apk'))

        desired_caps = {
            #'app': app,
            'appPackage': 'com.tencent.mm',
            'appActivity': 'com.tencent.mm.ui.LauncherUI',
            #'appActivity': 'com.tencent.mm.plugin.account.ui.WelcomeActivity',
            'platformName': 'Android',
            'platformVersion': PLATFORM_VERSION,
            'deviceName': '9f348b37',  # emulator-22 It's True
            'automationName': 'UiAutomator2',
            #'newCommandTimeout': 90,  # default 60s
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            #'autoWebviewTimeout': 3000,
            #'autoWebview': True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.loginWechat()

    def loginWechat(self):
        self.driver.implicitly_wait(10)
        button_login = self.driver.find_element_by_name(u'语言')
        # sleep(20)
        button_login.click()
        sleep(1)
        self.driver.find_elements_by_xpath('//android.widget.CheckBox')[4].click()
        self.driver.find_element_by_name(u'保存').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name('Log In').click()
        self.driver.find_element_by_name('Log in via WeChat ID/Email/QQ ID').click()
        username = self.driver.find_element_by_name('WeChat ID/Email/QQ ID')
        sleep(0.3)
        username.send_keys(YOUR_QQ)
        sleep(0.3)
        password = self.driver.find_element_by_id('com.tencent.mm:id/lh')
        sleep(0.3)
        password.send_keys(YOUR_PASSWORD)

        self.driver.find_element_by_name('Log In').click()
        self.driver.implicitly_wait(30)
        try:
            self.driver.find_element_by_name('No').click()
        except:
            pass
        self.driver.implicitly_wait(300)  # 必须?

        try:
            self.driver.find_element_by_name('Not Now').click()
        except:
            pass
        self.driver.implicitly_wait(300)  # 必须?

        self.driver.find_element_by_name('Discover').click()
        sleep(1)
        self.driver.find_element_by_name('Moments').click()
        sleep(3)
        self.getall()

    def getall(self):
        start = time.time()
        while True:
            # swipe down
            self.driver.swipe(start_x=520, start_y=1000, end_x=520, end_y=0, duration=400)  # duration越小，swipe跨度越大
            end = time.time()
            if end - start > 15:
                logging.info('See you !')
                break
        self.driver.quit()

if __name__ == '__main__':
    Wechat().__int__()





