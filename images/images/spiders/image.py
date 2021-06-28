import scrapy
from urllib.parse import urlencode
import json
import re
from ..items import TuwoItem

class ImageSpider(scrapy.Spider):

    name = 'image'

    allowed_domains = ['image.so.com']
    # start_urls = ['http://image.so.com/']
    def start_requests(self):

        for i in range(1,20):
            url = "https://twb.turawstock.com/api/photo/get_photo?label=%E5%B7%A5%E5%9C%B0%E5%AE%89%E5%85%A8%E5%B8%A6&kind=0&page=" + str(i)
            req = scrapy.Request(url=url, callback=self.parse)
            yield req

    def parse(self, response):

        tuwo = TuwoItem()


        imgurl_list = response.json()

        imgurl = imgurl_list['data']['photo_list']
        for x in imgurl:
            imgurll = x['thumb_w_url_cos']
            tuwo['img_url'] = imgurll

            yield tuwo
