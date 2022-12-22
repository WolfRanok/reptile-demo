import urllib.request
import urllib.parse

# 以百度访问为例
"""Handler处理器
定制更高级的请求头（随着业务逻辑的复杂请求对象的定制已经满足不了我们的需求(动态
cookie和代理不能使用请求对象的定制)
"""
url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 1.获取Handler处理器对象
handler = urllib.request.HTTPHandler()

# 2.获取opener对象
opener = urllib.request.build_opener(handler)

# 3.调用open
if __name__ == '__main__':
    with opener.open(request) as response:
        content = response.read().decode('utf-8')
        print(content)
