#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2019/11/13 17:39
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : signDemo.py
@Software : PyCharm Community
"""
import requests

_client_id = '40023368'
_fund_account = '40023368'
_stock_account = 'A603481950'


def getAccountInfo(self):
    fix_args = f"id=1&sqlId=Tool_Account_FIXFIRSTTRADEDATEUFDB&fund_account={_fund_account}"
    url = "http://172.28.25.54:21101/db/v3/call?" + fix_args
    print(url)
    requests.get(url)

def fixSTDeal(_client_id,_fund_account,_stock_account):
    fix_args = f"id=1&sqlId=Tool_Account_FIXFIRSTTRADEDATEUFDB&fund_account={_fund_account}"
    url = "http://172.28.25.54:21101/db/v3/call?" + fix_args
    print(url)
    requests.get(url)

    account_args = f"id=1&sqlId=Tool_Account_VIEWOFSTOCKHOLDER&asset_prop=0&exchange_type=1&fund_account={_fund_account}"
    url = "http://172.28.25.54:21101/db/v3/call?" + account_args
    print(url)
    requests.get(url)

    asset_args = f"id=1&sqlId=Tool_Asset_FIXAVERAGEASSETS&fund_account={_fund_account}"
    url = "http://172.28.25.54:21101/db/v3/call?" + asset_args
    print(url)
    requests.get(url)

    t2_331396_args = f"id=1&op_branch_no=1000&op_entrust_way=4&op_station=;&password=111111&fid=331396&fund_account={_fund_account}&client_id={_client_id}&stock_account={_stock_account}"
    url = "http://172.28.25.54:21101/t2?" + t2_331396_args
    print(url)
    requests.get(url)

fixSTDeal(_fund_account,_client_id,_stock_account)