import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ScrapyTest5ReadbookItem

class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1617.html']

    # 这里的follow参数为True时可以抓取所有潜在的url链接
    rules = (
        Rule(LinkExtractor(allow=r'/book/1617_\d+\.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        name = response.xpath('//div[@class="book-info"]//img/@alt').extract()
        src = response.xpath('//div[@class="book-info"]//img/@data-original').extract()
        for x,y in zip(name,src):
            book = ScrapyTest5ReadbookItem(name=x,src=y)
            yield book
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
