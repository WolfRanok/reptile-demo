import urllib.request
import urllib.parse
import json

url = r'https://fanyi.baidu.com/transapi'

# post 请求
headers = {
    'Cookie': 'BAIDUID=FDC94E6D08897017C9BDA37B7682927F:FG=1; BIDUPSID=05C48591C626E5CE264B69C58FAC7E45; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=kFSWFhrUVJOYURyb0J4M0otSi1OdEJFTFp-TDlXUnRBMC12OXcyTDYxRi1YckJpRVFBQUFBJCQAAAAAAQAAAAEAAABKN1EjxsbSuVlRWQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH7RiGJ-0YhiU; PSTM=1653197404; APPGUIDE_10_0_2=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1671351325,1671373304,1671373924,1671406187; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BA_HECTOR=01012h8l042l8h840la58fje1hptkq91g; ZFY=zbi:BzTuZAHzbZUswi9ru2F7w1sZ1Ga5yEjR1Cv9Ath8:C; RT="z=1&dm=baidu.com&si=xj6cn38uous&ss=lbt3ow21&sl=0&tt=0&ld=vpuu&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ul=vr7e&hd=vrbh"; __bid_n=18524ba40fb15b7f734207; FEID=v10-8b6755ac71b4aa66bdf6a943f26d4c1267033ee9; __xaf_fpstarttimer__=1671356085541; __xaf_ths__={"data":{"0":1,"1":43200,"2":60},"id":"202ec6bf-b7f5-4eca-9c5f-6d204a4dce98"}; __xaf_thstime__=1671356085813; FPTOKEN=ZbbH0GZe37K5Ib68baogVE7I93aWlu41bx2TCH1iGFpU93vUoqAy0ktQIxfyG8vs8KphfN3epgY+MUfOGoqJrwSeJ63ZZF1cihthpVOW4K5MN7mkasixhQieOevIRMA6K+tGVq1ufSDp/4zX9SBQeoLMh9FaBYdepgYWvvL9dn7At1IHCFUNdGtVM84VLA5KdqfK4oZMW91pwNhSPdfdyNlkmToRkTr3s8Yze0ocEiFiNF6+a52/r2Ep5LT4mwI/amCAF8C4S5bTCI1523IpvdCNgVAtrBNwI8olyEPSEpY73XaFPRsdUJsncPXJvp8/RYE7d9VoLTuU4L11e+XyQqRg0Z2uB7TOYE1046Nv7dWXCvK7mLEiPP8PP02Gmo4yafXB9c7uRpBY/pKduqb0TA==|0V/heiCWuxzM8Nmo6RL6PA8bO1YB0iEYB1e4pDewWMw=|10|2f8935f4123b2d54bd44f19385e25cc2; __xaf_fptokentimer__=1671356085963; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1671406984; ab_sr=1.0.1_MDY1ODE3YzVjMGEzMThmMDk3MzU1ODY3YmI1NGRkZGVkNTIyYmExZWFmNDRlMzZhMTkwZjA0MDhmYWYxNjJhODU5MDE1N2NmODY2NTk1YTA0ODg5YTZiYjI2MGY5MTI0NWY2ZmY0NzQ2MGI5YjFmY2JhYTE5NTE1YWY3ODY3ZDY3YjAxODUzNGRhZmUzYTkyM2RhNmU3MGJkYTY3M2U2N2FlM2JiYjYwMjJhZmFlYTg5NDUwZmNlNTY2NTkwMWNj',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
}

data = {
    'from': "zh",
    'to': "en",
    'query': "世界",
    'source': "txt"
}

# post请求的参数必须经过编码
data = urllib.parse.urlencode(data).encode('utf-8')  # urlencode返回字符串类型，所以还要一次编码转为二进制

# 请求对象的定制
# post请求的参数是不会拼接在URL的后面的
request = urllib.request.Request(url=url, data=data, headers=headers)

if __name__ == '__main__':
    # 模拟浏览器向服务器发送请求
    with urllib.request.urlopen(request) as response:
        content = response.read().decode()
        content = json.loads(content)
        res = json.loads(content['result'])['content'][0]['mean']
        print(res)
