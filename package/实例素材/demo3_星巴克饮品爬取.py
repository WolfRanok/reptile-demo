# -*- coding=gbk -*-
import random
from lxml import etree
import urllib.request
import urllib.parse


class spider:
    url = 'https://www.starbucks.com.cn/menu/'

    headers = {
        'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'Cookie': 'ZHh6ku4z = A6AltT6FAQAAow4VbdyBHymLfwfF3UawWQ2zph3mXENqGcFMNwwd0xxz9rmgASer1gCucm46wH8AAEB3AAAAAA | 1 | 0 | 6    dbc571d2dac947b02a530cccc780a7a8a141116',
    }

    # 代理池
    proxies_pool = [
        {'http': '138.43.105.139:80'},
        {'http': '92.247.142.182:35944'},
        {'http': '13.235.232.208:80'},
        {'http': '185.245.81.140:12444'},
        {'http': '117.54.11.82:3128'},
        {'http': '104.129.206.159:8800'},
    ]

    def create_request(self, url):
        request = urllib.request.Request(url=url, headers=self.headers)
        return request

    def get_content(self, request):
        proxies = random.choice(self.proxies_pool)

        handler = urllib.request.ProxyHandler(proxies=proxies)

        opener = urllib.request.build_opener(handler)

        with opener.open(request) as response:
            content = response.read().decode('utf-8')
        return content

    def save(self, content):
        with open('dates/星巴克饮品.html', 'w', encoding='utf-8') as f:
            f.write(content)

    def __init__(self):
        request = self.create_request(self.url)
        content = self.get_content(request)
        self.save(content)


"""
solution用于解析html
"""
class solution:

    def read_html(self):
        with open('dates/星巴克饮品.html', 'r', encoding='utf-8') as f:
            res = f.read()
        return res

    def analysis(self, content, config):
        tree = etree.HTML(content)

        res = tree.xpath(config)

        return res

    def __init__(self):
        res = self.read_html()
        print(self.analysis(res,'//ul[@class="grid padded-3 product"]/li/a/strong/text()'))


if __name__ == '__main__':
    solution()
