#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/12/27 10:34
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : paraDemo.py
@Software : PyCharm Community
"""

s = {
    "blurb": "https://ayfileres.yjbtest.com/IadvisorProjectImageUpload/29ELKDEtmQnANjhGV5277-24.png",
    "img_url": "https://ayfileres.yjbtest.com/IadvisorProjectImageUpload/rlQy3dOCoejx6eU3rD11e-23.png",
    "loveNum": 15,
    "name": "接口自动化请勿修改",
    "recommendWeight": 77,
    "recommended_reason": "接口自动化工作室推荐理由",
    "risk_warning": "本工作室相关服务内容仅供参考，投资者据此操作盈亏自负，<br/>股市有风险，入市需谨慎。\n<br/>更多风险提示，请在签约时查看协议内容。\n",
    "sort": 1,
    "waring_level": "R3"
}

l = list((map(str.lower, s.items())))


print(l)


