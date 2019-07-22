#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
import asyncio

# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(5)
#     print('Hello again! (%s)' % threading.currentThread())

async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")

loop = asyncio.get_event_loop()
tasks = [hello(), hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()