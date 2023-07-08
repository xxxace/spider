# scrapy框架
# 爬虫中封装好的一个明星框架。功能:高性能的持久化存储，异步的数据下载、高性能的据解析、分布式
# mac or linux: pip install scrapy
# windwos:
# -pip install wheel
# -下载twisted 下载地址为http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
# -安装twisted pip install Twisted-17.1.0-cp36-cp36m-win amd64.whl
# -pip install pywin32
# -pip install scrapy
# 测试：终端输入scrapy -v看看有没有报错

# 以上都是旧版本安装方法，还是以官网最新为准

# 创建项目：scrapy startproject xxxx
# 创建爬虫: scrapy genspider hello www.helloworld.com
# 执行爬虫：scrapy crawl hello --nolog
# 终端持久化存储，只能是parse的返回值被存储 csv json jsonlines jl xml marshal pickle
# scrapy crawl hello -o ./quibai.csv
# 基于管道持久化存储
# 可以使用yield 递归调用处理多页的情况
# if xxx <= xxx:
#   yield scrapy.Request(url=url, callback=self.parse)

# 五大核心组件

# 引擎(Scrapy)
# -用来处理整个系统的数据流处理触发事务(框架核心)

# 调度器(Scheduler)
# -用来接受引擎发过来的请求,压入队列中,并在引擎再次请求的时候返回,可以想像成一个URL(抓取网页的网址或者说是链接 )的优先队列，由它来决定下一个要抓取的网址是什么，同时去除重复的网址

# 下载器(Downloader)
# -用于下载网页内容,并将网页内容返回给蜘蛛(Scrapy下载器是建立在twisted这个高效的异步模型上的)

# 爬虫(Spiders)
# -爬虫是主要干活的,用于从特定的网页中提取自己需要的信息,即所谓的实体(tem)，用户也可以从中提取出链接让Scrapy继续抓取下一个页面

# 项目管道(Pipeline)
# -负责处理爬虫从网页中抽取的实体，主要的功能是持久化实体、验证实体的有效性、清除不需要的信息。当页面被爬虫解析后，将被发送到项目管道，并经过几个特定的次序处理数据。

# 请求传参 scrapy.Request(url=url, callback=self.parse, meta={'item':item})

# 图片数据处理ImagesPipeline
# https://docs.scrapy.org/en/latest/topics/media-pipeline.html#custom-images-pipeline-example

# 中间件
# 拦截请求：
#   -UA伪装
#   -代理IP
# 拦截响应
#   -篡改响应对象或数据