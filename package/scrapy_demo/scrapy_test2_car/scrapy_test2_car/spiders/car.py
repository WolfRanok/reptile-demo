import scrapy


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['www.autohome.com.cn']
    start_urls = ['http://www.autohome.com.cn/']

    def parse(self, response):
        print('='*10)
        xpath_text = response.xpath('//div/a')
        print(xpath_text.extract())
