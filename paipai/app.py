#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/7/2 15:55
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : app.py
@Software : PyCharm Community
"""

from PyWeChatSpy import WeChatSpy
import random
import re


def my_parser(data):
    if data["type"] == 5: # 判断是微信消息数据
        for msg in data["data"]:  # 遍历微信消息
            if msg["msg_type"] == 10000:  # 判断是微信拍一拍系统提示
                # 因为微信系统消息很多 因此需要用正则匹配消息内容进一步过滤拍一拍提示
                # {'self': 0, 'msg_type': 10000, 'wxid1': '179xxxxxx72@chatroom', 'content': '"Mandy的小脑袋" 拍了拍你'}
                m = re.search('".*" 拍了拍我', msg["content"])
                if m:  # 搜索到了匹配的字符串 判断为拍一拍
                    image_path = f"D:\learngit\PythonTest\paipai\images\{random.randint(1, 7)}.jpg"  # 随机选一张回复用的图片
                    spy.send_file(msg["wxid1"], image_path)  # 发送图片

spy = WeChatSpy(parser=my_parser)  # 实例化WeChatSpy类


if __name__ == '__main__':
    spy.run()  # 运行代码