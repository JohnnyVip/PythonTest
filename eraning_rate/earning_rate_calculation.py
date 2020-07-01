#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/4/16 17:05
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : earning_rate_calculation.py
@Software : PyCharm Community
"""

import xlrd
from xlutils.copy import copy

def read_excel(src:str,index:int)->tuple:
    """
    读取excel
    :param src:
    :param index:
    :return:
    """
    # 打开文件
    wb = xlrd.open_workbook(src,formatting_info=True)

    # sheet索引从0开始，得到sheet1表的句柄
    sheet2 = wb.sheet_by_index(index)

    # 行数
    rowNum = sheet2.nrows

    # 列数
    colNum = sheet2.ncols

    return rowNum,colNum,sheet2


def write_excel(des:str,src:str,index:int,day_rate_list:list,cumulative_rate_list:list)->None:
    """
    数据写入excel
    :param des:源目录
    :param src:目的目录
    :param index:
    :param day_rate_list:
    :param cumulative_rate_list:
    :return:
    """
    # 打开文件
    workbook = xlrd.open_workbook(src,formatting_info=True)

    # sheet索引从0开始，得到sheet1表的句柄
    sheet2 = workbook.sheet_by_index(index)

    # 行数
    rowNum = sheet2.nrows

    # 列数
    colNum = sheet2.ncols

    wb = copy(workbook)
    sheet = wb.get_sheet(1)

    # 输入数据
    for i in range(2,rowNum):
        sheet.write(i,colNum-1,cumulative_rate_list[i-2])
        sheet.write(i,colNum-2,day_rate_list[i-2])

    # 保存
    wb.save(des)

def day_rate(rowNum:int,colNum:int,sheet:xlrd.sheet.Sheet)->list:
    """
    日收益率函数
    :param rowNum:
    :param colNum:
    :param sheet:
    :return:
    """
    # 账户日收益率
    day_rate_list = []

    # 股票数
    stock_num = colNum - 3

    for i in range(2, rowNum):
        cnt = 0
        sum_x = 0.0
        avg_x = 0.0
        # colNum - 2 股票数读取控制
        for j in range(1, colNum-2):
            var_type = sheet.cell(i, j).ctype
            var = sheet.cell(i, j).value
            if var_type and var:
                sum_x = sum_x + sheet.cell(i, j).value
                avg_x = sum_x / stock_num
        day_rate_list.append(avg_x)
    return day_rate_list

def cumulative_rate(day_rate_list: list, day: int)->float:
    """
    累计收益率函数
    :param day_rate_list:
    :param day:day:1,2,3 第day天
    :return:
    """
    # 累计收益率
    cu_rate = 0
    for i, avg_x in enumerate(day_rate_list):
        if i == day - 1:
            cu_rate = (1 + cu_rate) * (1 + avg_x) - 1
            break
        cu_rate = (1 + cu_rate) * (1 + avg_x) - 1
    return cu_rate

def get_cumulative_rate_list(day_rate_list:list)->list:
    """
    累计收益率列表
    :param day_rate_list:
    :return:
    """
    cumulative_rate_list = []
    for i in range(1,len(day_rate_list)+1):
        cumulative_rate_list.append(cumulative_rate(day_rate_list,i))
    return cumulative_rate_list

def main():
    rowNum,colNum,sheet2 = read_excel(src=r'D:\learngit\PythonTest\eraning_rate\测试客户账户.xls', index=1)
    day_rate_list = day_rate(rowNum=rowNum,colNum=colNum,sheet=sheet2)
    print(day_rate_list)
    cu_rate = cumulative_rate(day_rate_list=day_rate_list,day=1)
    cumulative_rate_list = get_cumulative_rate_list(day_rate_list=day_rate_list)
    print(cumulative_rate_list)
    write_excel(des=r'D:\learngit\PythonTest\eraning_rate\测试客户账户_bak.xls',src=r'D:\learngit\PythonTest\eraning_rate\测试客户账户.xls',index=1,day_rate_list=day_rate_list,cumulative_rate_list=cumulative_rate_list)

if __name__ == '__main__':
    # print(read_excel(src=r'C:\Users\Administrator\Desktop\测试客户账户.xls',index=1))
    # rowNum,colNum,sheet2 = read_excel(src=r'C:\Users\Administrator\Desktop\测试客户账户.xls', index=1)
    # day_rate_list = day_rate(rowNum=rowNum,colNum=colNum,sheet=sheet2)
    # print(day_rate_list)
    # cu_rate = cumulative_rate(day_rate_list=day_rate_list,day=1)
    # cumulative_rate_list = get_cumulative_rate_list(day_rate_list=day_rate_list)
    # print(cumulative_rate_list)
    # write_excel(src=r'C:\Users\Administrator\Desktop\测试客户账户.xls',index=1,day_rate_list=day_rate_list,cumulative_rate_list=cumulative_rate_list)
    main()
    pass