# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TuchongsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class tu_baoc(scrapy.Item):
    img_url = scrapy.Field()
    name = scrapy.Field()