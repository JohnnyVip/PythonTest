#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/4/14 10:33
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : list2DictDemo.py
@Software : PyCharm Community
"""
import re

source_data = ['测试场景', '开户首页banner图定制展示验证', '验证点', '优先级验证：（活动编码+渠道编码）均匹配>活动编码匹配>渠道编码匹配', '测试用例', '配有上线（渠道编码+活动编码）、活动编码、渠道编码的图片，优先展示（渠道编码+活动编码）的图片', '测试步骤',
               '1.后台配置5张上线图片：图片1（活动编码a，渠道编码b）、图片2（活动编码a，渠道编码c）、图片3（活动编码d，渠道编码b）、图片4（活动编码a，渠道编码空）、图片5（活动编码空，渠道编码b）\n2.客户端打开URL1：活动编码为a、渠道编码为b\n3.客户端打开URL2：活动编码为a、渠道编码为c\n4.客户端打开URL3：活动编码为d，渠道编码为b\n5.客户端打开URL4：活动编码为a、渠道编码为空\n6.客户端打开URL5：活动编码为空、渠道编码为b\n7.客户端打开URL6：活动编码为空、渠道编码为空',
               '数据构造', 'ims平台>运营相关>开户首页Banner管理——新增\nURL：https://fzwebapps.yjbtest.com/yjbwebguide/guide/web/guide/view/index.html?channel_type=a&activity_no=b', '预期结果',
               '2.展示图片1\n3.展示图片2\n4.展示图片3\n5.展示图片4\n6.展示图片5\n7.展示默认图片', '优先级', 'M', '测试环境','设计人员', '王亚玲', '测试人员','测试结论', '备注']

def list2Dict(data:list):
    """
    列表的特定元素->字典
    :param txt: 列表
    :return:
    """
    dict_var = []
    for ele in data:
        if isinstance(ele,str) and ele.startswith('1'):
            re_str = re.findall(r".(.+?)\n", ele)
            for d in re_str:
                var = d.split("：",1)
                dict_list = {var[0]:var[1]}
                dict_var.append(dict_list)

    return dict_var

print(list2Dict(data=source_data))




