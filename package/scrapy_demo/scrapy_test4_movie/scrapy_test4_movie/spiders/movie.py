import scrapy
from ..items import ScrapyTest4MovieItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['dytt8.net']
    start_urls = ['https://dytt8.net/html/gndy/china/index.html']

    def parse(self, response):
        # 爬取第一页法名字与第二页的图片
        name = response.xpath('//div[@class="co_area1"]/div[@class="co_content2"]/ul/a/text()').extract()
        src = response.xpath('//div[@class="co_area1"]/div[@class="co_content2"]/ul/a//@href').extract()
        for new_name, y in zip(name, src):
            new_url = 'http://www.dytt8.net' + y

            # 对第二个链接进行访问，写一个新的函数用于引用
            # 注意这里已经进入到新的url地址里面了
            yield scrapy.Request(url=new_url, callback=self.parse_second, meta={"name": new_name})

    def parse_second(self, response):
        content = response.xpath('//div[@id="Zoom"]//img/@src').extract()
        name = response.meta['name']
        src = content[0]
        movie = ScrapyTest4MovieItem(name=name, src=src)
        return movie
