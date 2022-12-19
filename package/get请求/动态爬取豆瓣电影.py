import json
import urllib.request
import urllib.parse

"""
爬取10页的豆瓣电影（动作）
"""
headers = {
    'Cookie': 'bid=Me3Yue5iUlc; ll="108304"; __yadk_uid=0MMMEzEWzIYarbWDyWmnTQWX22nKqhxj; _pk_id.100001.4cf6=1722d40b178d29c7.1670321188.2.1671457158.1670321188.; __utma=30149280.210981012.1670321188.1670321188.1671457148.2; __utmz=30149280.1671457148.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.752911900.1670321188.1670321188.1671457148.2; __utmz=223695111.1671457148.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1671457147%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DsR5CdrC8ntUhJu3LrTZKTMJWxJHoDgVYRcJ_sXkxkT_KS6lpRs_wKppUZRj4xj9s%26wd%3D%26eqid%3Dddc30721000222ec0000000563a06975%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utmb=30149280.0.10.1671457148; __utmc=30149280; __utmb=223695111.0.10.1671457148; __utmc=223695111; __gads=ID=3e372ca5175e89e6-225802d09ad900ac:T=1671457149:RT=1671457149:S=ALNI_MYB4sa5QfUSYtf_JiYS5k10qwcGVQ; __gpi=UID=00000b93f8504acd:T=1671457149:RT=1671457149:S=ALNI_MZx6fz0h3GSX0AUOvgSnbkllpSLLA',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
}

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&'


def get_json(num):
    """
    :param num: str
    :return: json
    """
    # get请求的参数只能在URL中找到，而不会在（浏览器包的）请求中找到
    data = {
        "start": num * 20,
        "limit": 20
    }

    # 请求对象定制(get请求无需用unicode进行编码)
    url_demo = url + urllib.parse.urlencode(data)

    requests = urllib.request.Request(url=url_demo, headers=headers)
    # 获取响应数据
    with urllib.request.urlopen(requests) as response:
        content = response.read().decode('utf-8')
    # print(content,type(content))
    # 下载数据
    return json.loads(content)


if __name__ == '__main__':
    dates = []
    for i in range(10):
        data = get_json(i)
        dates.append(data)

    # 将json数据转为字符串，就可以随意存储了
    with open('dates/豆瓣电影.json', 'w+', encoding='utf-8') as f:
        json.dump(dates, f, ensure_ascii=False, indent=4)
