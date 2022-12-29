import requests

class ScrapyTest3DangdangPipeline:

    def open_spider(self, spider):
        self.f = open('../dates/book.txt', 'w+')

    # item就是yield后面的book对象(类似字典)
    def process_item(self, item, spider):
        self.f.writelines(str(item))
        return item

    def close_spider(self, spider):
        self.f.close()


# 多条管道同时开启
# 定义管道类
# 在setting中开启管道
class DangDangSpiderPipelines:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
    }

    def process_item(self, item, spider):
        url = item['src']
        name = '../dates/' + item['name'] + '.jpg'

        with requests.get(url=url, headers=self.headers) as response:
            content = response.content
        with open(name,'wb') as f:
            f.write(content)

        return item
