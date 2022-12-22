import random
import urllib.request

from lxml import etree


# 1. 解析本地文件
def local():
    content = ''
    with open('dates/快代理.html', 'r', encoding='utf-8') as f:
        content = f.read()
    # 这里理论上应该是使用etree.parse,但是etree.parse对html的文件语法检查太严格了，无法正常读取
    tree = etree.HTML(content)

    # xpath查找语句
    res = tree.xpath('//div/div/ul/li[@data-id="dps"]/@data-menu')
    print(res)


# 2. 使用现爬的数据

def Cloud():
    url = 'https://www.baidu.com'

    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64; x64; rv: 104.0) Gecko / 20100101 Firefox / 104.0'
    }

    # 代理池
    proxies_pool = [
        {'http': '121.13.252.60:41564'},
        {'http': '120.24.76.81:8123'}
    ]

    # 请求对象的定制
    request = urllib.request.Request(url=url, headers=headers)

    # 动态代理
    proxies = random.choice(proxies_pool)
    handler = urllib.request.ProxyHandler(proxies=proxies)
    opener = urllib.request.build_opener(handler)

    # 模拟浏览器访问服务器
    with opener.open(request) as response:
        content = response.read().decode('utf-8')

    tree = etree.HTML(content)

    res = tree.xpath('//a')
    print(res)


if __name__ == '__main__':
    Cloud()
