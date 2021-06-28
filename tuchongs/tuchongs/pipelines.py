# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import requests
import time

class TuchongsPipeline:
    def process_item(self, item, spider):
        return item


class img_URL_baoc(object):
    def process_item(self, item, spider):

        # 将返回的值再用get请求返回二进制
        req=requests.get(url=item['img_url'])

        # 用时间函数当随机名称
        x = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

        # 拼接本地地址
        url = r"E:\python_script\tuchongs\images" + "\\" + item['name'] + x + '.jpg'

        # 保存图片
        with open(url,"wb") as f:
            f.write(req.content)