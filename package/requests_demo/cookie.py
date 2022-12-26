import ddddocr
from lxml import etree
import requests

"""
通过登录，进入到主界面
在页面中寻找参数值不定的量

---面为某次登录时的参数表---

__VIEWSTATE	"Gil/8XCb9q5L0HMsSiNx+3I9rvNDox6QkJ6qtTAzc80Da+HGpMZ5iye4gyQbt0msDScI9ZYRJbr4qmVL/L5AI9PESC9zjLSBNmIc89zqHXCL/8+okQGd+AKGos1lDmD44h8J58jqoQ4AhWuyzKyZamIUrMM="
__VIEWSTATEGENERATOR	"C93BE1AE"
from	"http://so.gushiwen.cn/user/collect.aspx"
email	"13819501004"
pwd	"ranok6666"
code	"ls21"
denglu	"登录"

"""

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
}

data = {
    '__VIEWSTATE': '',
    '__VIEWSTATEGENERATOR': '',  # 这两个参数待补充
    "from": "http://so.gushiwen.cn/user/collect.aspx",
    "email": "13819501004",
    'pwd': "ranok6666",
    'code': "",  # 验证码需要手动输入
    'denglu': "登录"
}

session = requests.Session()


# 用于获取__VIEWSTATEGENERATOR，与__VIEWSTATE参数
def get_parameter():
    # 这个是登录界面的地址
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

    with session.get(url=url, headers=headers) as response:
        content = response.text

    tree = etree.HTML(content)
    __VIEWSTATE = tree.xpath('//input[@name="__VIEWSTATE"]/@value')[0]
    __VIEWSTATEGENERATOR = tree.xpath('//input[@name="__VIEWSTATEGENERATOR"]/@value')[0]
    data['__VIEWSTATE'] = __VIEWSTATE
    data['__VIEWSTATEGENERATOR'] = __VIEWSTATEGENERATOR
    return content


def get_img(url):
    with session.get(url=url, headers=headers) as response:
        img = response.content
    return img


# 获取验证码图片
def get_verification(content):
    # 这是一个登录接口
    tree = etree.HTML(content)
    img_url = 'https://so.gushiwen.cn/' + tree.xpath('//img[@id="imgCode"]/@src')[0]

    with open('dates/验证码.jpg', 'wb') as f:
        f.write(get_img(img_url))


# 验证码识别
def Crack():
    ocr = ddddocr.DdddOcr()
    with open('dates/验证码.jpg', 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    return res


def login():
    url = 'http://so.gushiwen.cn/user/collect.aspx'
    code = Crack()
    data['code'] = code

    with session.post(url=url, headers=headers, data=data) as response:
        content = response.text

    with open('dates/古文网.html', 'w', encoding='utf-8') as f:
        f.write(content)
    tree = etree.HTML(content)
    print(tree.xpath('//a'))
    return content


if __name__ == '__main__':
    login_content = get_parameter()
    get_verification(login_content)
    login()
