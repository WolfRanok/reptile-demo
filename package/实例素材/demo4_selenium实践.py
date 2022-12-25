# -*- coding=gb2312 -*-
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

"""
用selenium实现对百度的交互
"""


def wait(func):
    def res(self, *args):
        time.sleep(1)
        func(self, *args)

    return res


class spider:
    path = 'chromedriver.exe'
    url = 'https://www.baidu.com'

    def create_browser(self, url):
        """
        创建浏览器访问对象
        :return: None
        """
        browser = webdriver.Chrome(self.path)
        browser.get(url)  # 打开输入的网址
        return browser

    def get_obg(self, id, name):
        return self.browser.find_element(id, name)

    def __init__(self):
        self.browser = self.create_browser(self.url)
        self.input = self.get_obg('id', 'kw')  # 找到搜索文本框
        self.input.send_keys('周杰伦')  # 向元素中传入参数

        time.sleep(2)

        self.button = self.get_obg('id','su')
        # 点击按钮
        self.button.click()

        time.sleep(2)

        # 滚轮滑动到底部
        js1 = "window.scrollTo(0, document.body.scrollHeight)"
        self.browser.execute_script(js1)

        time.sleep(2)

        # 获取下一页的按钮
        self.next = self.browser.find_element(by=By.XPATH,value='//a[@class="n"]')
        self.next.click() # 点击下一页

        time.sleep(2)

        # 回到上一页
        self.browser.back()

        input()



if __name__ == '__main__':
    spider()
