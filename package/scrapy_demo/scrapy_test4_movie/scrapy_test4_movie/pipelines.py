# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import requests
from itemadapter import ItemAdapter


class ScrapyTest4MoviePipeline:
    def get_img(self,url):
        return requests.get(url=url).content

    def process_item(self, item, spider):
        img = self.get_img(item['src'])
        name = '../dates/' + item['name'] + '.jpg'
        with open(name,'wb') as f:
            f.write(img)

        return item
