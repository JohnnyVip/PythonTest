#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/7/12 19:26
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : testTT.py
@Software : PyCharm Community
"""
from time import sleep
import time
import sys
from appium import webdriver
PLATFORM_VERSION = '6.0.1'

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
            # 'autoWebview': True, ##不能用
            "noReset": True
        }
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
