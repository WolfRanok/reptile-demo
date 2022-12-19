import urllib.parse
import urllib.request
import json

url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Cookie': 'BAIDUID=FDC94E6D08897017C9BDA37B7682927F:FG=1; BIDUPSID=05C48591C626E5CE264B69C58FAC7E45; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=kFSWFhrUVJOYURyb0J4M0otSi1OdEJFTFp-TDlXUnRBMC12OXcyTDYxRi1YckJpRVFBQUFBJCQAAAAAAQAAAAEAAABKN1EjxsbSuVlRWQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH7RiGJ-0YhiU; PSTM=1653197404; APPGUIDE_10_0_2=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1671373304,1671373924,1671406187,1671450288; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; __bid_n=18527d3ce9e6214ced4207; FEID=v10-597dd420c73485ac46d512841c6dcddaf622dc6f; __xaf_fpstarttimer__=1671437123537; __xaf_ths__={"data":{"0":1,"1":43200,"2":60},"id":"73164daa-75ab-433c-a952-d0221d497064"}; __xaf_thstime__=1671437123905; FPTOKEN=z9XjSBXSDeFgJAf9IDNHzO/uSk6N+/k9n8tzm5DPiEAZbmSqVQG0oau4ON9Q+D8vy317emW9lMJmvQS77WTNnzQUcnLs8oNrTxyxJCObC0H56cJv4O1XEhO0RJ3oDRtK8BUSVwPEhBga0LsDOuYDeGSsagh3mNPdIq1fLy4eIfZxgS0webtjrxLnujUJH5yeMIedk+ipqRG9lxaGA2olM5rL/IuZT/ash+/MUYv0vjYdaXKfZ/CIcCbm8vIj3bxprBxtAFJ5P9ZXkDji71GaXgKKiVYJS3cDcxgsWLwKeiq3kiM+vqB3W+SCLz39wETI+01bz8SJhF/hzS8EDbsvuRRzp/kLezsaDMn4T2K5UeK6yOW6NMTedoFPivxkMFogJIh1U7091HkfuQrJmSybtg==|pnAAqIwun41GGP5mBIx6brbh/vd1fcP0McKBR3DZzac=|10|e1b6bdf6a699f634c92479c12b3148bc; __xaf_fptokentimer__=1671437123906; BA_HECTOR=0h0h0k8g2h8laga0258k2qvi1hq0aj11h; ZFY=zbi:BzTuZAHzbZUswi9ru2F7w1sZ1Ga5yEjR1Cv9Ath8:C; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1671450833; ab_sr=1.0.1_YzMxMjdmMDc3MzdiNjg1MDM1N2FkYWRkOGM2ZTZjZjIxMzkyYTdjNTA5MGRhZDlkN2EzYzY3NjE5OGU2NDZhYzA4MTE0YWEyYzg0NGM0N2Y4YTZjMDkxMjVjMjcwNDU2ZmUwN2Q4OGQ2YzE1NzU2NzkwNTY4YzAwYzkzZGJlOGU3MzY5YjFiODljYzM2OTZmMjYxYzYwYmY2MWM0MThjMzhlY2IwMTNiNmEzYjU4OTU4NzAyZWE3YWYxODUwNGIx',
}

data = {
    'from': "zh",
    "to": "en",
    "query": "你在寻找什么",
    "transtype": "enter",
    "simple_means_flag": "3",
    "sign": "345305.108520",    # 这个参数会因为翻译内容的改变而改变，所以这个爬虫无法推广
    "token": "764e97f3e9a499a03408c6b2f172f51d",
    "domain": "common"
}

# 转二进制编码
data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url=url, headers=headers, data=data)

if __name__ == '__main__':
    with urllib.request.urlopen(request) as response:
        content = json.loads(response.read().decode('utf-8'))
        print(content)
