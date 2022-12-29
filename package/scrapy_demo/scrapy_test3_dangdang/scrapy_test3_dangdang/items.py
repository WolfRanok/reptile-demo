# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyTest3DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 将定义的数据放入下面
    src = scrapy.Field()    # 图片链接
    name = scrapy.Field()   # 名字
    price = scrapy.Field()  # 价格