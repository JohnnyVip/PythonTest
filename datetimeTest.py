# !/usr/bin/env python3
# -*- coding:utf-8 -*-
from datetime import datetime, timedelta, timezone

now = datetime.now()

print(now)

t = now.timestamp()

print(now.timestamp())

tz_utc_8 = timezone(timedelta(hours=8))

dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00

print(dt)

print(dt.timestamp())

print(datetime.utcfromtimestamp(t))

