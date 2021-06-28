import requests
from urllib.request import urlretrieve
import time
import os


def image_spider(key_q, key_ps, key_sn):  # 请求函数
    url = "http://image.so.com/j?q=nba&src=srp&correct=nba&pn=60&ch=&sn=208&ps=201&pc=60&pd=1&prevsn=148&sid=39b8dabeae51031efce5a8d8b1fc6957&ran=0&ras=6&cn=0&gn=0&kn=8&comm=1 "
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        'Referer': "http://image.so.com/i?q=nba&src=srp"
    }
    params = {
        'q': key_q,
        'src': 'srp',
        'pn': '60',
        'ch': '',
        'sn': key_sn,
        'ps': key_ps,
        'pc': '60',
        'pd': '1',
        'prevsn': '0',
        'sid': 'd34ad660320d853f00ea2d476ba2eaa5',
        'ran': '0',
        'ras': '6',
        'cn': '0',
        'gn': '0',
        'kn': '8',
        'comm': '1'
    }

    response = requests.get(url, headers=headers, params=params).json()  # 转json
    lists = response.get('list')  # 提取list件，值为一个列表

    for lis in lists:
        open_image(lis.get('img'))  # 遍历列表，提取其中img字符串（图片url）
    time.sleep(2)


def open_image(image_url):
    image_name = hash(image_url)  # 图片名字（为图片地址的url值）
    path_1 = r'E:\360image'
    if not os.path.exists(path_1):
        os.mkdir(path_1)
    path = path_1 + '\%s.jpg' % str(image_name)  # 图片地址
    urlretrieve(image_url, path)  # 保存图片
    print(image_url, '下载成功')
    time.sleep(1)


def main():
    key_q = input("输入要爬取的图片关键词:")
    ps = 81
    sn = 88

    for i in range(0, 10):  # 爬取多少图片
        key_ps = ps + i * 60
        key_sn = sn + i * 60
        image_spider(key_q, key_ps, key_sn)


if __name__ == '__main__':
    main()
