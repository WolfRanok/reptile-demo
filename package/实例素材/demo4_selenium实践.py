# -*- coding=gb2312 -*-
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

"""
��seleniumʵ�ֶ԰ٶȵĽ���
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
        ������������ʶ���
        :return: None
        """
        browser = webdriver.Chrome(self.path)
        browser.get(url)  # ���������ַ
        return browser

    def get_obg(self, id, name):
        return self.browser.find_element(id, name)

    def __init__(self):
        self.browser = self.create_browser(self.url)
        self.input = self.get_obg('id', 'kw')  # �ҵ������ı���
        self.input.send_keys('�ܽ���')  # ��Ԫ���д������

        time.sleep(2)

        self.button = self.get_obg('id','su')
        # �����ť
        self.button.click()

        time.sleep(2)

        # ���ֻ������ײ�
        js1 = "window.scrollTo(0, document.body.scrollHeight)"
        self.browser.execute_script(js1)

        time.sleep(2)

        # ��ȡ��һҳ�İ�ť
        self.next = self.browser.find_element(by=By.XPATH,value='//a[@class="n"]')
        self.next.click() # �����һҳ

        time.sleep(2)

        # �ص���һҳ
        self.browser.back()

        input()



if __name__ == '__main__':
    spider()
