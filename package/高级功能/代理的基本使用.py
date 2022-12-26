import urllib.request
import urllib.parse

url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=monline_7_dg&wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

## 代理
# 代理网址：https://www.kuaidaili.com/free/
# 必须与url的协议对上
proxies = {
    'https': '121.13.252.60:41564'
}

handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

if __name__ == '__main__':
    with opener.open(request) as response:
        content = response.read().decode('utf-8')

    with open('dates/data1.html','w',encoding='utf-8') as f:
        f.write(content)