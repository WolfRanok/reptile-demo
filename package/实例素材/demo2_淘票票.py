# -*- coding=gb2312 -*-
import random
import json
import jsonpath
import urllib.parse
import urllib.request

"""
本案例用于爬取，淘票票官网上的城市信息
"""


# 用这个类把json数据爬取下来
class spider:
    url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1671788434148_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

    headers = {
        'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9',
        'bx-v': '2.2.3',
        'cookie': 't=5dcf5aa119c121c2a0bc93807b093fd5; cookie2=10821310525552356211d1f3f185e5e3; v=0; _tb_token_=fb16576418bee; cna=X+ApGiUcDTkCAduMOyO/3YEs; xlly_s=1; l=fBNNAA9eT-cLlcwWBOfZPurza77OtIRYouPzaNbMi9fPOv1H5zgcW6SW3vYMCnGVFs5BJ3yZyToBBeYBqC2sjqj4axom4lDmnmOk-Wf..; tfstk=cnEFBRZZQMIU61eRMcmz7aAdcz0dZUw3Ehkj-_rbh3X1MVuhird-IcgIQY9wZ2f..; isg=BCkpAC1Sbv2ACFJJTENJAvYXONWD9h0ooITEtsse6JBPkkmkEkbj-EGMVDakDLVg',
        'referer': 'https://dianying.taobao.com/',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
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

    def __init__(self):
        request = self.create_request(self.url)
        content = self.get_content(request)


if __name__ == '__main__':
    with open('dates/城市.json','r') as f:
        res = f.read()
    res = json.loads(res)
    t = jsonpath.jsonpath(res,'$..regionName')
    print(t)
