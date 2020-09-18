import requests
from urllib.parse import urlencode
import os
from hashlib import md5


def get_page(offset, keywords):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': keywords,
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab'
    }
    url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&' + urlencode(params)
    response = requests.get(url)
    # 500服务器内部错误，400错误请求（服务器找不到请求的语法） 404未找到
    if response.status_code == 200:
        print(response.json())
        return response.json()


def get_images(json):
    data = json.get('data')
    if data:
        for item in data:
            image_list = item.get('image_list')
            title = item.get('title')

            if image_list:
                for image in image_list:
                    # 构造一个生成器，将图片和标题一起返回
                    yield {
                        'image': image.get('url'),
                        'title': title
                    }


# item就是get_image()返回的一个字典
# item里面的title创建一个文件夹
def save_image(item):

    local_image_url = item.get('image')
    response = requests.get(local_image_url)

    if response.status_code == 200:
        file_path = r'E:\toutiao'
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        file_path = file_path + '\{0}.{1}'.format(md5(response.content).hexdigest(), 'jpg')

        # 判断路径是否存在，如果不存在，写入
        if not os.path.exists(file_path):
            with open(file_path, 'wb')as f:
                f.write(response.content)


# 定义一个offset数组，遍历，提取图片，下载
def main(offset, keywords):
    json = get_page(offset, keywords)
    for item in get_images(json):
        print(item)
        save_image(item)


if __name__ == '__main__':
    keywords = input("请输入要爬取图片的关键词:")
    offset = input("请输入要爬取的数量:")
    main(offset, keywords)
