import json
import urllib.request
import urllib.parse

"""
带着cookie话，相当于是保留了一份登录的信息，在下次使用的时候可以跳过登录的流程
本demo就是针对这个做的爬虫
"""
url = 'http://kb.chaoxing.com/res/pc/curriculum/schedule.html?s=61e4a791727a236a1834981b5aeeb164'

headers = {
    'Cookie': 'fid=170118; lv=0; _uid=192200107; uf=b2d2c93beefa90dc7cbcaf879eb42210924d42fe10f75a07d01327b4d4a43fe12de8e0d48059ada5b3e6debb40aabeecf4670332ccec4baa17a3131c5323ef268f160e7a6d7807818b3e6e5f395dd3564129e2925200b376625a1e432617356fe56abed66b8915cee7fafd565af53bf2; _d=1670407586934; UID=192200107; vc=C5CE5754058B0FEC35AEAC6AEA27B0DB; vc2=67CBFEB61FD78595F61B46B218F47701; vc3=Rti%2BHldP6tmiO8Rg7hU6xYLb5A2slPswKGlPh10179wI4yQH1C1sww21F88aMlUWYn7XrKK9fDlM8bfPAAYxX6mGs5V2HEJAi%2BuORGg9oBz29n4AFI1RtLQLoB9arquxawAh9fTAZanEe4%2BAYLc51boguGp%2FH%2BF0Eo0aQMoyWU0%3D1e1f790e51d4cdf0a3f55fe8e4ff83c9; xxtenc=67d0f4b2c527d838142625d24881539e; DSSTASH_LOG=C_38-UN_2181-US_192200107-T_1670407586936; tl=1; spaceFid=170118; spaceRoleId=""; JSESSIONID=F79B0EE69663A0B58DE2F6A02E2380FA.CurriculumService; route=353349bf0fa5580c2c23247980829e03',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Referer': 'http://i.chaoxing.com/',
}

# 定制请求对象
request = urllib.request.Request(url=url, headers=headers)

if __name__ == '__main__':
    with urllib.request.urlopen(request) as response:
        content = response.read().decode('utf-8')
        print(content)
