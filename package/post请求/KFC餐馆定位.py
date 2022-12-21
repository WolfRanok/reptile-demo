import urllib.parse
import urllib.request
import json

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'route-cell=ksa; SERVERID=7b574a5ee35938b607213c6a1c6f2c4a|1671537216|1671536924; ASP.NET_SessionId=5jndydxbqympimbxf0as4sl0; Hm_lvt_1039f1218e57655b6677f30913227148=1671536924; Hm_lpvt_1039f1218e57655b6677f30913227148=1671536924'
}


def get_json(num):
    """
    :param num:int
    :return: json
    """
    data = {
        "cname": "杭州",
        "pid": "",
        'pageIndex': num,
        'pageSize': "10"
    }
    # 将参数进行unicode编码
    data = urllib.parse.urlencode(data).encode('utf-8')

    # 定制请求对象
    request = urllib.request.Request(url=url,data=data,headers=headers)

    with urllib.request.urlopen(request) as response:
        content = response.read().decode('utf-8')

    return json.loads(content)



if __name__ == '__main__':
    dates = []
    for i in range(5):
        dates.append(get_json(i))

    with open('dates/KFC.json','w+',encoding='utf-8') as f:
        json.dump(dates,f,ensure_ascii=False,indent=4)