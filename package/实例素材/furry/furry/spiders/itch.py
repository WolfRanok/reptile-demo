import scrapy
from ..items import FurryItem

class ItchSpider(scrapy.Spider):
    name = 'itch'
    allowed_domains = ['itch.io']
    start_urls = ['https://itch.io/games/tag-furry']

    def parse(self, response):
        titles = response.xpath('//div[@class="game_cell_data"]/div[@class="game_text"]/@title').extract()
        img = response.xpath('//div[@class="game_thumb"]/a[@class="thumb_link game_link"]/img/@data-lazy_src').extract()
        for title,img in zip(titles,img):
            wolf = FurryItem(title=title,img=img)
            yield wolf

