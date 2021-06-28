# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from . import settings
import os
import requests
import time

class ImagesPipeline:
    def process_item(self, item, spider):
        return item

class ImgDownloadPipeline(ImagesPipeline):

    def process_item(self, item, spider):

        req = requests.get(url=item['img_url'])
        x = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        url = r"E:\\python_script\\images\\images\\imagesss" + "\\" + x + '.jpg'

        with open(url, "wb") as f:
            f.write(req.content)