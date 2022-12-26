from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    path = r"C:\Users\17627\AppData\Local\Google\Chrome\Application\chrome.exe"

    chrome_options.binary_location = path

    browser = webdriver.Chrome(chrome_options=chrome_options)

    return browser


## 以上为固定格式，无论在什么情况下，只要用这个就可以做到无界面的网页模拟 ##

browser = get_browser()

url = 'https://www.baidu.com'

browser.get(url=url)

browser.save_screenshot('dates/baidu.png')
