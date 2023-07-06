import asyncio
import time

urls = [
    'https://www.baidu.com',
    'https://www.sogou.com',
    'https://v2.cn.vuejs.org',
    'https://v2.cn.vuejs.org',
    'https://v2.cn.vuejs.org',
    'https://v2.cn.vuejs.org',
    'https://v2.cn.vuejs.org',
    'https://v2.cn.vuejs.org',
    'https://v2.cn.vuejs.org',
    'https://v2.cn.vuejs.org',
    'https://v2.cn.vuejs.org',
    'https://v2.cn.vuejs.org',
    'https://v2.cn.vuejs.org',
    'https://v2.cn.vuejs.org',
    'https://v2.cn.vuejs.org'
]


async def request(url):
    print('开始请求：', url)
    await asyncio.sleep(2)
    print('请求结束')

tasks = []
loop = asyncio.new_event_loop()

for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c, loop=loop)
    tasks.append(task)


loop.run_until_complete(asyncio.wait(tasks))
