# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy


# class ImgsproPipeline:
#     def process_item(self, item, spider):
#         return item


class imgsPileLine(ImagesPipeline):

    # 根据图片地址进行图片数据请求
    def get_media_requests(self, item, info):

        yield scrapy.Request(item['src'])

    # 指定图片存储路径
    def file_path(self, request, response=None, info=None, *, item=None):
        imgName = request.url.split('/')[-1]
        return imgName


    def item_completed(self, results, item, info):
        # 返回给下一个即将被执行的管道类
        return item
