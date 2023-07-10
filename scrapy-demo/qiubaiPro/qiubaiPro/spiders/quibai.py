import scrapy
from qiubaiPro.items import QiubaiproItem
from selenium import webdriver
from selenium.webdriver import ChromeOptions


class QuibaiSpider(scrapy.Spider):
    name = "quibai"
    # allowed_domains = ["www.xxx.com"]
    start_urls = [
        "https://developers.weixin.qq.com/community/develop/doc/00022c683e8a80b29bed2142b56c01?page=1#comment-list"]

    # def parse(self, response):
    #     # 解析：评论者 + 内容 + 日期
    #     li_list = response.xpath('//*[@id="comment-list"]/div/div/ul/li')

    #     comment_list = []

    #     for li in li_list:
    #         name = li.xpath('./a/span/span/strong/text()')[0].extract()
    #         avatar_src = li.xpath(
    #             './a/span/span/div[@class="post_comment_owner_avatar"]/img/@src')[0].extract()
    #         comments = li.xpath('./div[3]//text()')
    #         comment = ''
    #         for comment_text in comments:
    #             comment += comment_text.extract()

    #         date = li.xpath(
    #             './span[@class="post_comment_pos"]/span[@class="post_comment_time"]/text()')[0].extract()

    #         comment_list.append({
    #             "name": name,
    #             "avatar_src": avatar_src,
    #             "comment": comment,
    #             "date": date
    #         })

    #     return comment_list
    
    def start_requests(self):
        browser_option = ChromeOptions()
        # 无头浏览器（即不显示浏览器）
        browser_option.add_argument('--headless')
        browser_option.add_argument('--disable-gpu')
        # 实现规避检测
        browser_option.add_experimental_option(
            'excludeSwitches', ['enable-automation']
        )
        # 创建selenium浏览器
        self.browser = webdriver.Chrome(options=browser_option)
        return super().start_requests()

    def parse(self, response):
        # 解析：评论者 + 内容 + 日期
        li_list = response.xpath('//*[@id="comment-list"]/div/div/ul/li')

        for li in li_list:
            name = li.xpath('./a/span/span/strong/text()')[0].extract()
            avatar_src = li.xpath(
                './a/span/span/div[@class="post_comment_owner_avatar"]/img/@src')[0].extract()
            comments = li.xpath('./div[3]//text()')
            comment = ''
            for comment_text in comments:
                comment += comment_text.extract()

            date = li.xpath(
                './span[@class="post_comment_pos"]/span[@class="post_comment_time"]/text()')[0].extract()

            item = QiubaiproItem()
            item['name'] = name
            item['avatar_src'] = avatar_src
            item['comment'] = comment
            item['date'] = date
            # 将item提交给管道
            yield item

    def closed(self, reason):
        print('self', self)
        print('reason', reason)
        print('closeddddddddddddddddddddddddddddddd')
        self.browser.quit()
