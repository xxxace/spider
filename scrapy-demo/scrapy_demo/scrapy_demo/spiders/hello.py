import scrapy


class HelloSpider(scrapy.Spider):
    name = "hello"
    # 一般不用，除非只爬该域名下的网站
    # allowed_domains = ["www.helloworld.com"]
    # 爬取的网站列表
    start_urls = ["https://www.helloworld.com"]

    # 响应结果解析,每处理一个start_urls里的链接就触发一次。
    def parse(self, response):
        pass
