import scrapy
from douban.items import DoubanItem

class DbanSpider(scrapy.Spider):
    name = 'dban'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):

        div_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li/div')

        for div in div_list:

            item = DoubanItem()

            item['rank'] = div.xpath('./div[1]/em/text()').get()
            item['title'] = div.xpath('./div[2]/div[1]/a/span[1]/text()').get()

            yield item