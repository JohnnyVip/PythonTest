#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/6/16 15:19
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : GetAllHyperLinks.py
@Software : PyCharm Community
"""

import requests
import re

class GetAllHyperLinks(object):

    #存放html字符串
    __content = None

    def __init__(self,url=None):
        self.__url = url

    # 获取html网页资源
    def getResource(self):
        _res = requests.get(self.__url)
        GetAllHyperLinks.__content = _res.text

    # 对_content中url进行过滤
    @classmethod
    def urlFilter(cls):
        # 匹配url的regex
        pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        hyperlinks = re.findall(pattern, cls.__content)
        return hyperlinks

    #显示所有url
    @staticmethod
    def showUrl():
        #hyperlinks是一个存储url的列表
        hyperlinks = GetAllHyperLinks.urlFilter()
        print("count(url):"+str(len(hyperlinks)))
        i = 0
        for url in hyperlinks:
            i += 1
            print("["+str(i)+"]:"+url+'\n')

def main():

    #新建任务对象
    task = GetAllHyperLinks("http://www.Gjzq.com.cn")

    #获取网页资源
    task.getResource()

    #过滤url
    GetAllHyperLinks.urlFilter()

    #显示url条目
    GetAllHyperLinks.showUrl()

if __name__ == '__main__':
    main()
