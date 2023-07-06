import asyncio
import time


async def request(url):
    print('url:', url)
    time.sleep(0.2)
    print('成功请求！')
    return url


def callback_func(task):
    print('回调：', task.result())


# async修饰的函数调用后会返回一个协程对象
c = request('xxxxx')
c2 = request('xxxxx2')
c3 = request('xxxxx3')

# 获取事件循环对象
event_loop = asyncio.new_event_loop()
asyncio.set_event_loop(event_loop)
# 将协程对象注册到事件循环中，然后启动loop
event_loop.run_until_complete(c)

# 创建task
task = event_loop.create_task(c2)
event_loop.run_until_complete(task)

# 创建futrue
task = asyncio.ensure_future(c3, loop=event_loop)
# 绑定回调
task.add_done_callback(callback_func)
event_loop.run_until_complete(task)
