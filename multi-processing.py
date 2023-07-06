# 解决中文乱码问题
# 1.response.encoding = 'utf-8'
# 2.img_name.encode('iso-8859-1').decode('gbk')

# Python爬虫验证码识别免费开源版
# pip install ddddocr

# 使用session对象来保存会话记录。每次发送都会收集和携带cookie
# session = requests.session()
# session.get() session.post()

# 代理
# page_text = requests.get(url=url, headers=headers, proxies={"https": "xxxxxxxxx"})

# 异步爬虫
# -多线程、多进程（无节制版-不建议使用）：
# -好处：为相关阻塞的单独操作开启多线程、多进程来解决阻塞，从而达到异步执行
# -弊端：开启多线程、多进程会消耗CPU资源，导致服务器慢等问题

# -线程池、进程池（适当使用）：
# -原则：阻塞且较为耗时才使用
# -好处：可以减少开启或销毁线程和进程的频率，从而减少对系统的开销
# -弊端：有数量的限制

# -单线程+异步协程（推荐）：
# event_loop: 事件循环
# coroutine: 协程对象
# task：任务，对协程任务的封装，包含了任务的各个状态
# future: 代表了将来要执行，但现在还没有执行的任务，和task没有本质上的区别
# async: 定义一个协程
# await：挂起阻塞的方法
# request.get 是同步的，ai0http 是异步的用于异步协程开发

# 导入线程池模块对应的类
from multiprocessing.dummy import Pool
import time

start_time = time.time()


def get_page(str):
    print("执行开始：", str)
    time.sleep(2)
    print("下载成功：", str)
    return str+'.py'


name_list = ['aa', 'bb', 'cc', 'dd', 'ee']
# 开启4个线程
pool = Pool(4)
result = pool.map(get_page, name_list)
end_time = time.time()
print(end_time - start_time)
print(result)
