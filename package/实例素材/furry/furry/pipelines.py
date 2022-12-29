# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

import requests
from itemadapter import ItemAdapter


class FurryPipeline:
    def open_spider(self, spider):
        self.f = open('../dates/furry_game.json', 'w', encoding='utf-8')
        self.data = []

    def process_item(self, item, spider):
        self.data.append([item['img'], item['title']])
        return item

    def close_spider(self, spider):
        json.dump(self.data, self.f, indent=4)
        self.f.close()


def load_img(url, title):
    with requests.get(url=url) as response:
        content = response.content
    src = 'dates/' + title + '.jpg'
    try:
        with open(src, 'wb') as f:
            f.write(content)
    except:
        print("error : "+src)


if __name__ == '__main__':
    with open(r'dates/furry_game.json', 'r', encoding='utf-8') as f:
        res = json.load(f)
    for [x,y] in res:
        load_img(x,y)
