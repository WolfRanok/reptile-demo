import json

import jsonpath
import requests

url = 'https://fanyi.baidu.com/transapi'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Cookie': 'BAIDUID=FDC94E6D08897017C9BDA37B7682927F:FG=1; BIDUPSID=05C48591C626E5CE264B69C58FAC7E45; BDUSS=kFSWFhrUVJOYURyb0J4M0otSi1OdEJFTFp-TDlXUnRBMC12OXcyTDYxRi1YckJpRVFBQUFBJCQAAAAAAQAAAAEAAABKN1EjxsbSuVlRWQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH7RiGJ-0YhiU; PSTM=1653197404; BD_UPN=13314752; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BA_HECTOR=818l81052k2h84ah2h018hg51hqdjv21j; ZFY=WZDt62awEhs9BN8nmAxMedvC7rmz8nhghgAIaZ4lpcs:C; COOKIE_SESSION=12382_0_6_7_13_8_1_0_5_4_0_4_12257_0_2_0_1671885049_0_1671885047%7C9%2340_35_1671707677%7C9; BD_HOME=1; H_PS_PSSID=36552_37974_37647_37517_37910_37623_36921_37872_37948_37938_37953_37902_26350_37788_37881; BDRCVFR[Hp1ap0hMjsC]=mk3SLVN4HKm; delPer=0; BD_CK_SAM=1; PSINO=3; H_PS_645EC=2672DSPeWXMEeTOse1jOSBzSf7BMSueWxYi8ph3TfKnU1BjWedGXWBQtCJW7wrVhQ7ue; baikeVisitId=45aa72ca-32cc-4f11-888e-5884e0df157f; B64_BOT=1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
}

data = {
    'from': "en",
    "to": "zh",
    'query': "word",
    'source': "txt"
}

with requests.post(url=url, data=data, headers=headers) as response:
    response.encoding = 'utf-8'
    content = response.text
    content = json.loads(content)['result']
    content = json.loads(content)
    res = jsonpath.jsonpath(content, '$..content..mean..cont')

    print(content)
    print(res)
