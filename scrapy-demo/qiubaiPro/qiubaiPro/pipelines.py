# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class QiubaiproPipeline:
    fp = None

    # 重写父类方法
    def open_spider(self, spider):
        print('开始爬')
        self.fp = open('./quibai.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        name = item['name']
        avatar_src = item['avatar_src']
        comment = item['comment']
        date = item['date']

        self.fp.write(name+'\n'+avatar_src+'\n'+comment+'\n'+date+'\n\n')
        return item

    def close_spider(self, spider):
        print('结束爬')
        self.fp.close()


class MysqlPipeline:
    conn = None
    cursor = None
    inser_sql = 'insert into comment (name,avatar_src,comment,date) values(%s,%s,%s,%s)'
    # 重写父类方法

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='123456', db='wx_mp')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        name = item['name']
        avatar_src = item['avatar_src']
        comment = item['comment']
        date = item['date']

        try:
            values = (name, avatar_src, comment, date)
            self.cursor.execute(self.inser_sql, values)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
