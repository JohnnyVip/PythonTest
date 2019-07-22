#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# encoding:utf-8

import json

data = {"status": "OK", "count": 2, "results": [{"age": 27, "name": "Oz", "lactose_intolerant": True}, {"age": 29, "name": "Joe", "lactose_intolerant": False}]}
json_data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))
print(json_data)
