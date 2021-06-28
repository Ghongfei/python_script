import scrapy
from ..items import tu_baoc
import re

class TuchongSpider(scrapy.Spider):
    name = 'tuchong'
    # allowed_domains = ['stock.tuchong.com']
    # start_urls = ['https://tuchong.com/']

    def start_requests(self):

        for i in range(1,20):
            url = "https://premium.tuchong.com/search?term=%E5%B7%A5%E4%BA%BA%E9%AB%98%E7%A9%BA%E4%BD%9C%E4%B8%9A&no_overwrite=&use=0&type=&layout=&sort=0&category=0&page={}&size=100&search_from=&exact=0&platform=creativevip&tp=&abtest=&royalty_free=0&image_source=&photographerId=0&photographerName=&option=&tiff_size_from=0&tiff_size_to=0&color=&has_person=0&face_num=&gender=0&age=&racial=&samemodel=0&price=0&image_format=&is_need_overwrite=true".format(i)
            req = scrapy.Request(url=url, callback=self.parse)
            yield req

    def parse(self, response):

        t = tu_baoc()
        imagIds = re.compile('"imageId":"(.*?)"')

        results = imagIds.finditer(response.text)
        for r in results:
            imgurl = 'https://icweiliimg1.pstatp.com/weili/smh/{}.jpg'.format(r.groups()[0])

            t['img_url'] = imgurl
            t['name'] = r.groups()[0]

            yield t
