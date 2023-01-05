from selenium import webdriver

"""
一些网页中它的标签是在网页中通过请求（如js）来不断充实的，所以可以用selenium实现
可以真实的模拟打开浏览器，这样就不存在
"""

# 创建浏览器操作对象
path = 'chromedriver.exe'
browser = webdriver.Chrome()

url = 'https://www.baidu.com'


# selenium查找元素对象的方式
def find(id, val):
    # 使用属性名,属性的方式来寻找标签
    button = browser.find_element(id, val)
    return button


# 访问元素信息，即获取标签中的属性
def information(obj, name):
    # 指定对象的标签名查找对应的属性值
    print(obj.get_attribute(name))
    print(obj.tag_name)  # 获取标签的名字
    print(obj.text)  # 元素的文本信息


if __name__ == '__main__':
    browser.get(url)
    button = find('id', 'su')
    information(button, 'type')
    input()
