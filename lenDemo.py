#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/1/3 9:40
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : lenDemo.py
@Software : PyCharm Community
"""

a = {
    "code": 0,
    "message": "null",
    "result": [
        {
            "activityTime": True,
            "channel_type": "RJB",
            "contractDescription": "成功签约投顾服务工作室的客户，通过在国金证券开立的账户进行沪深A股、信用账户A股、场内基金交易时，佣金率均为0.6‰",
            "link_id": 71,
            "name": "股衍罗盘",
            "nowDate": "null",
            "rate_plan": {
                "contract_type": "DUE_ADJUST",
                "end_time": "2020-06-06 23:59:59",
                "is_Delete": "NOT_DELETE",
                "name": "股衍罗盘长期签约",
                "original_price": 0.001,
                "pay_price": 6.0E-4,
                "pay_type": "COMMISSION_RATE",
                "service_Flag": "IS_FOREVER",
                "service_cycle": -1,
                "start_time": "2019-11-01 00:00:00"
            },
            "rate_plan_list": "null",
            "studio": {
                "blurb": "https://ayfileres.yongjinbao.com.cn/IadvisorProjectImageUpload/jEe8axeILKKb24uADWbZQ-9726.png",
                "img_url": "https://ayfileres.yongjinbao.com.cn/IadvisorProjectImageUpload/eZvn1jqtxnzVdVFOx1vWR-9901.png",
                "loveNum": 89,
                "name": "股衍罗盘",
                "recommendWeight": 0,
                "recommended_reason": "股票加期权，守正出奇，穿越牛熊。股衍罗盘投顾服务工作室欢迎您！",
                "risk_warning": "本工作室相关服务内容仅供参考，投资者据此操作盈亏自负，股市有风险，入市需谨慎。\n更多风险提示，请在签约时查看协议内容。\n",
                "sort": 3,
                "waring_level": "R3"
            },
            "studioStatus": "RECOMMEMD_STUDIO",
            "type": "STUDIO"
        }
    ]
}

print(a["result"].__len__())
