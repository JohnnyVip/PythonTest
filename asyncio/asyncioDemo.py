import asyncio


@asyncio.coroutine
def get_html(url, name):
    print("%s get %s html start" % (name, url))
    yield from asyncio.sleep(2)
    print("%s get %s html end" % (name, url))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # 创建两个协程
    tasks = [
        get_html("http://www.baidu.com", "A"),
        get_html("http://www.souhu.com", "B"),
    ]
    # 启动事件循环并将协程放进去执行
    loop.run_until_complete(asyncio.wait(tasks))