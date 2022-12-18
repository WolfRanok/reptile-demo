import urllib.request
import urllib.parse

'''
urlencode 应用场景: 存在多个参数的时候
可以将字典中的多个中文转为Unicode,并以网页请求的方式连接起来
'''

url = 'https://www.baidu.com/baidu?'  # 千万要注意这里不能把最后一个‘?’给省略了

data = {
    "wd": "周杰伦",
    'sex': '男'
}

headers = {
    'Cookie': 'BAIDUID=FDC94E6D08897017C9BDA37B7682927F:FG=1; BIDUPSID=05C48591C626E5CE264B69C58FAC7E45; BDUSS=kFSWFhrUVJOYURyb0J4M0otSi1OdEJFTFp-TDlXUnRBMC12OXcyTDYxRi1YckJpRVFBQUFBJCQAAAAAAQAAAAEAAABKN1EjxsbSuVlRWQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH7RiGJ-0YhiU; PSTM=1653197404; BD_UPN=13314752; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=37855_36552_37517_36921_37910_37831_37623_37872_37949_37938_37953_37902_26350_37788_37881; BA_HECTOR=01012h8l042l8h840la58fje1hptkq91g; delPer=0; BD_CK_SAM=1; PSINO=3; ZFY=zbi:BzTuZAHzbZUswi9ru2F7w1sZ1Ga5yEjR1Cv9Ath8:C; COOKIE_SESSION=1409_0_7_5_10_20_0_2_7_6_1_10_1764_0_258_0_1671353420_0_1671353162%7C9%2315649_35_1671257136%7C9; RT="z=1&dm=baidu.com&si=xj6cn38uous&ss=lbt3ow21&sl=0&tt=0&ld=vpuu&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ul=vr7e&hd=vrbh"; BDRCVFR[Hp1ap0hMjsC]=mk3SLVN4HKm; __bid_n=18524ba40fb15b7f734207; ZD_ENTRY=baidu; FEID=v10-8b6755ac71b4aa66bdf6a943f26d4c1267033ee9; __xaf_fpstarttimer__=1671356085541; __xaf_ths__={"data":{"0":1,"1":43200,"2":60},"id":"202ec6bf-b7f5-4eca-9c5f-6d204a4dce98"}; __xaf_thstime__=1671356085813; FPTOKEN=ZbbH0GZe37K5Ib68baogVE7I93aWlu41bx2TCH1iGFpU93vUoqAy0ktQIxfyG8vs8KphfN3epgY+MUfOGoqJrwSeJ63ZZF1cihthpVOW4K5MN7mkasixhQieOevIRMA6K+tGVq1ufSDp/4zX9SBQeoLMh9FaBYdepgYWvvL9dn7At1IHCFUNdGtVM84VLA5KdqfK4oZMW91pwNhSPdfdyNlkmToRkTr3s8Yze0ocEiFiNF6+a52/r2Ep5LT4mwI/amCAF8C4S5bTCI1523IpvdCNgVAtrBNwI8olyEPSEpY73XaFPRsdUJsncPXJvp8/RYE7d9VoLTuU4L11e+XyQqRg0Z2uB7TOYE1046Nv7dWXCvK7mLEiPP8PP02Gmo4yafXB9c7uRpBY/pKduqb0TA==|0V/heiCWuxzM8Nmo6RL6PA8bO1YB0iEYB1e4pDewWMw=|10|2f8935f4123b2d54bd44f19385e25cc2; __xaf_fptokentimer__=1671356085963; H_PS_645EC=b63dhHbivu8%2FbVWZJtX79DBt3P9uBVNYwAcY%2Fg8415zSUhvu0JTYYIZBh10; baikeVisitId=23003255-8512-46b7-a87b-ebcf6699ec43; B64_BOT=1; BD_HOME=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
}

if __name__ == '__main__':
    url += urllib.parse.urlencode(data)
    print(url)
    # 请求对象的定制
    request = urllib.request.Request(url=url, headers=headers)

    # 获取请求对象
    with urllib.request.urlopen(request) as response:
        # 获取网页原码的数据
        content = response.read().decode('utf-8')
        print(content)