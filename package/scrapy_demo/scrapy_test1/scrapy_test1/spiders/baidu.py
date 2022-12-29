import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫使用的值
    name = 'baidu'
    # 允许访问的域名
    allowed_domains = ['www.baidu.com']

    # 起始的访问域名
    start_urls = ['http://www.baidu.com/']

    # 运行起始url之后执行的方法，方法中的response就是返回的请求对象
    # response=request.get()
    def parse(self, response):
        print("=======================")
