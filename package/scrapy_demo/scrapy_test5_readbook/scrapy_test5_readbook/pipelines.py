# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyTest5ReadbookPipeline:
    Hash = set()

    def open_spider(self, spider):
        self.f = open('../dates/name.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        book = str(item)
        if book not in self.Hash:
            self.Hash.add(book)
            self.f.writelines(book + '\n')
        return item

    def close_spider(self, spider):
        self.f.close()


# 用于加载setting文件
from scrapy.utils.project import get_project_settings
import pymysql


class MySqlPipeline:

    # 用于链接数据库
    def open_spider(self, spider):
        setting = get_project_settings()
        self.host = setting['DB_HOST']
        self.port = setting['DB_PORT']
        self.user = setting['DB_USER']
        self.passwrod = setting['DB_PASSWROD']
        self.name = setting['DB_NAME']
        self.charset = setting['DB_CHARSET']
        self.connect()

    # 用于数据库链接
    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.passwrod,
            db=self.name,
            charset=self.charset
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into book(name,src) values ("{}","{}")'.format(item['name'], item['src'])
        # 执行sql语句
        self.cursor.execute(sql)
        # 提交
        self.conn.commit()
        return item

    # 关闭数据库
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()