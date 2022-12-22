import re
from lxml import etree
import random
import urllib.request
import urllib.parse
import json

"""
网站加载图片等信息时，可能存在“懒加载”导致图片在一开始没加载而在加载的时候改变标签名导致爬取不成功
"""
class spider:

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
    }
    # 免费的代理对象
    proxies_pool = [
        {'http':'138.43.105.139:80'},
        {'http': '92.247.142.182:35944'},
        {'http': '13.235.232.208:80'},
        {'http': '185.245.81.140:12444'},
        {'http': '117.54.11.82:3128'},
        {'http': '104.129.206.159:8800'},
    ]

    def create_request(self, num):
        url = self.get_url(num)
        request = urllib.request.Request(url=url,headers=self.headers)
        return request

    def get_url(self, num: int) -> str:
        if num == 1:
            return 'https://sc.chinaz.com/tu/lang.html'
        return f'https://sc.chinaz.com/tu/lang-{num}-0-0.html'

    def get_content(self,request):
        proxies = random.choice(self.proxies_pool)

        handler = urllib.request.ProxyHandler(proxies=proxies)

        opener = urllib.request.build_opener(handler)

        with opener.open(request) as response:
            content = response.read().decode('utf-8')

        return content

    def get_image(self,url):
        request = urllib.request.Request(url=url, headers=self.headers)
        with urllib.request.urlopen(request) as response:
            content = response.read()

        with open(f'dates/image/lang{self.count}.jpg','wb') as f:
            f.write(content)
        self.count += 1

    def down_image(self,content):

        tree = etree.HTML(content)

        image_url = tree.xpath('//img[@class="preview"]/@data-src')
        image_url = ['https:' + x for x in image_url]
        image_url = [re.sub(r'\\','/',x) for x in image_url]

        for url in image_url:
            self.get_image(url)



    def __init__(self):
        self.count = 1
        request = self.create_request(1)
        content = self.get_content(request)
        self.down_image(content)


if __name__ == '__main__':
    spider()
