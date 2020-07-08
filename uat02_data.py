#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/6/19 17:24
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : uat02_data.py
@Software : PyCharm Community
"""

import requests

def clientId2Pid():
    """
    批量clientId换取pid
    :return:
    """

    sign_id = 2643183

    fr = open("client_id.txt", "r")

    for line in fr.readlines():  # 依次读取每行
        client_id = int(line.strip())  # 去掉每行头尾空白
        sign_id = sign_id + 2

        # 永久签约

        url = f"http://172.28.80.43:30000/yjbapi/iadviser/sign/new_forever_sign?studio_id=1&client_id={client_id}&device_no=&advisor_id=27&advisor_name=yaoqiang&channel=组合&product_code=P_002"

        payload = {}
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response1 = requests.request("GET", url, headers=headers, data=payload)

        print(response1.text.encode('utf8'))

        # 审核通过

        url = "http://172.28.25.54:21101/rpc/dubbo"

        payload = f'id=1&appName=investment-adviser-manager&interfaceName=com.sinolink.is.iadviser.manager.IadvisorSignService&method=approvePass&group=uat02&args=%5B%7B%22java.lang.Integer%22%3A{sign_id}%7D%2C%7B%22java.lang.String%22%3A%2215988884444%22%7D%2C%7B%22java.lang.String%22%3A%22yaoqiang%22%7D%5D'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response2 = requests.request("POST", url, headers=headers, data=payload)

        print(response2.text.encode('utf8'))

        # 退签
        url = "http://172.28.25.54:21101/rpc/dubbo"

        payload = f'id=1&appName=investment-adviser-manager&interfaceName=com.sinolink.is.iadviser.manager.IadvisorSignService&method=refundSign&group=uat02&args=%5B%7B%22java.lang.Integer%22%3A{sign_id}%7D%2C%7B%22java.lang.String%22%3A%2215988884444%22%7D%2C%7B%22java.lang.String%22%3A%2215988884444%22%7D%2C%7B%22java.lang.String%22%3A%22yaoqiang%22%7D%5D'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response3 = requests.request("POST", url, headers=headers, data=payload)

        print(response3.text.encode('utf8'))

    # 关闭文件
    fr.close()
    pass





