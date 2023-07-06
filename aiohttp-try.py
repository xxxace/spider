import aiohttp
import asyncio

urls = [
    'https://www.baidu.com',
    'https://www.sogou.com',
    'https://v2.cn.vuejs.org'
]


async def request(url):
    async with aiohttp.ClientSession() as session:
         async with session.get(url) as response:
            #   text() 字符串
            #   read() 二进制
            #   json() json
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")
    

tasks = []
loop = asyncio.get_event_loop()

for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c, loop=loop)
    tasks.append(task)


loop.run_until_complete(asyncio.wait(tasks))