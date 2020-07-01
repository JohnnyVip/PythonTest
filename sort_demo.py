#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time     : 2020/5/28 17:17
@Author   : Johnny
@Email    : yaoqiang@gjzq.com.cn
@File     : sort_demo.py
@Software : PyCharm Community
"""

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

def sort_func(rows:list,reverse:bool)->list:
    """
     对元素为dict的list进行排序
    :param rows:
    :param reverse: True:降序,False:升序
    :return:
    """
    # 新列表
    new_rows = []

    # uid 字典
    uid_dict = {}

    for i,ele in enumerate(rows):
        uid = ele["uid"]
        uid_dict[str(i)] = uid

    print(uid_dict.items())

    uid_list = sorted(uid_dict.items(), key=lambda k: k[1],reverse=reverse)

    # 组装新列表
    for uid_tuple in uid_list:
        new_rows.append(rows[int(uid_tuple[0])])

    return new_rows
    pass

if __name__ == '__main__':
    # print(sort_func(rows=rows,reverse=False))
    sorted_rows = sorted(rows, key=lambda k: k['uid'],reverse=True)
    print(sorted_rows)
