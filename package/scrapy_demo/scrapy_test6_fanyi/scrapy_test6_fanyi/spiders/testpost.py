import scrapy
import json

class TestpostSpider(scrapy.Spider):
    name = 'testpost'
    allowed_domains = ['fanyi.baidu.com']
    # post请求如果没有参数，那么这个请求将没有任何意义
    start_urls = ['https://fanyi.baidu.com/transapi']

    def parse(self, response):
        pass

    def start_requests(self):
        url = 'https://fanyi.baidu.com/transapi'
        data = {
            'from': "zh",
            'to': "en",
            'query': "你好",
            'source': "txt",
        }
        yield scrapy.FormRequest(url=url,formdata=data,callback=self.myParse)

    def myParse(self,response):
        content = json.loads(response.text)
        res = json.loads(content['result'])
        print(res)