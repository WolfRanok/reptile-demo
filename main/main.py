import urllib.request
import urllib.parse


# urllib.parse.quote 方法可以将中文转为Unicode的编码
url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=40020637_8_oem_dg&wd=' + urllib.parse.quote("周杰伦")

# 定制请求头(反爬的第一种手段)
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'Cookie': 'BIDUPSID=FB3E7C503913D26F0C7DDF40DB945F85; PSTM=1633263785; __yjs_duid=1_91cf8ac12dc2e3cdf7810c2d17da680b1633265202843; H_PS_PSSID=26350; BD_UPN=12314753; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[AC8fclRJDLs]=mk3SLVN4HKm; BAIDUID=A88CE6AF15D0D7281AFE03DFC6A2BF25:FG=1; delPer=0; BD_CK_SAM=1; PSINO=3; BA_HECTOR=0l008g2g0la584208hal8u6t1hprhcd1h; BAIDUID_BFESS=A88CE6AF15D0D7281AFE03DFC6A2BF25:FG=1; ZFY=B61J0fBgXlhtjk:BGckY:BbRZZmiSxVTnsaGNs:B5R6OL4:C; B64_BOT=1; H_PS_645EC=8d8dDKNikplVOgDijpxwK4GBT%2FYM5nWtt%2F%2FlC3jWRhEm3Z6LR%2B%2Bgqdz2RsHOxdt97jH4TppxbNs; baikeVisitId=c88e2f55-41c1-456b-8696-463eab7b44bd'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

if __name__ == '__main__':
    # 模拟浏览器向服务器发送请求
    with urllib.request.urlopen(request) as response:
        content = response.read().decode('utf-8')
        print(content)
