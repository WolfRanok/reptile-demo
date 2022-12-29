import scrapy
import json
import jsonpath
from ..items import ScrapyTest3DangdangItem


class DangSpider(scrapy.Spider):
    name = 'dang'
    allowed_domains = [
        'e.dangdang.com']
    start_urls = [
        'http://e.dangdang.com/media/api.go?action=mediaCategoryLeaf&promotionType=1&deviceSerialNo=html5&macAddr=html5&channelType=html5&permanentId=20210826092725989162205447730919174&returnType=json&channelId=70000&clientVersionNo=6.8.0&platformSource=DDDS-P&fromPlatform=106&deviceType=pconline&token=&start=0&end=5&category=QCWX&dimension=dd_sale&order=0']
    pageNum = 1

    def parse(self, response):
        print('=' * 20)
        content = json.loads(response.text)
        root = jsonpath.jsonpath(content, '$..data.saleList..mediaList')
        src = jsonpath.jsonpath(root, '$..coverPic')
        name = jsonpath.jsonpath(root, '$..authorPenname')
        price = jsonpath.jsonpath(root, '$..lowestPrice')
        for x, y, z in zip(src, name, price):
            book = ScrapyTest3DangdangItem(src=x, name=y, price=z)
            # 每一次都传一个数据过去给管道
            yield book

        # 一次爬取5本书本
        if self.pageNum < 20:  # 控制！否则无限递归了。。
            self.pageNum += 1
            url = f'http://e.dangdang.com/media/api.go?action=mediaCategoryLeaf&promotionType=1&deviceSerialNo=html5&macAddr=html5&channelType=html5&permanentId=20210826092725989162205447730919174&returnType=json&channelId=70000&clientVersionNo=6.8.0&platformSource=DDDS-P&fromPlatform=106&deviceType=pconline&token=&start={self.pageNum * 5}&end={self.pageNum * 5 + 5}&category=WX&dimension=dd_sale&order=0'
            yield scrapy.Request(url=url, callback=self.parse)
