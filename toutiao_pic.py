# import requests
# from urllib.parse import urlencode
# import os
# from hashlib import md5
# import re
# from multiprocessing.pool import Pool
# import time
#
# def get_page(offset):
#
#     global headers
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
#     }
#     params = {
#         'aid': '24',
#         'app_name': 'web_search',
#         'offset': offset,
#         'format': 'json',
#         'keyword': '工地安全帽',
#         'autoload': 'true',
#         'count': '20',
#         'en_qc': '1',
#         'cur_tab': '1',
#         'from': 'search_tab',
#         'pd': 'synthesis',
#         'timestamp': int(time.time()),
#     }
#     url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)
#     url = url.replace('=+', '=')
#
#     try:
#         response = requests.get(url,headers=headers,params=params)
#         response.content.decode('utf-8')
#
#         if response.status_code == 200:
#             print(response.json())
#             return response.json()
#     except requests.ConnectionError as e:
#         print(e)
#
#
# def get_images(json):
#     data = json.get('data')
#     if data:
#         for item in data:
#
#             image_list = item.get('article_url')
#             title = item.get('title')
#
#             req = requests.get(image_list, headers=headers)
#             if req.status_code == 200:
#                 pat = '<script>var BASE_DATA = .*?articleInfo:.*?content:(.*?)groupId.*?;</script>'  # 用正则大致匹配一下范围
#                 match = re.search(pat, req.text, re.S)
#                 if match != None:
#                     result = re.findall(r'img src&#x3D;\\&quot;(.*?)\\&quot;', match.group(), re.S)
#
#                     #  print(i.encode('utf-8').decode('unicode_escape')
#                     # 转换编码方式 把\u之类的改掉
#                     yield {
#                         'title': title,
#                         'image': result
#                     }
#
# # item就是get_image()返回的一个字典
# # item里面的title创建一个文件夹
# def save_image(item):
#
#     file_path = r'E:\Crawling\toutiao'
#     if not os.path.exists(file_path):
#         os.mkdir(file_path)
#
#     for title_str,url_img in enumerate(item['image']):
#         url_img = url_img.encode('utf-8').decode('unicode_escape')
#         response = requests.get(url_img, headers=headers)
#
#     if response.status_code == 200:
#
#         file_path = file_path + '\{0}.{1}'.format(md5(response.content).hexdigest(), 'jpg')
#
#         # 判断路径是否存在，如果不存在，写入
#         if not os.path.exists(file_path):
#             try:
#                 with open(file_path, 'wb')as f:
#                     f.write(response.content)
#             except:
#                 print('error')
#
#
# # 定义一个offset数组，遍历，提取图片，下载
# def main(offset):
#     json = get_page(offset)
#     for item in get_images(json):
#         print(item)
#         save_image(item)
#
#
# if __name__ == '__main__':
#     pool = Pool()
#     groups = [j * 20 for j in range(8)]
#     pool.map(main, groups)  # 传offset偏移量
#     pool.close()
#     pool.join()



import requests
from urllib.parse import urlencode  # 构造url
import time
import os
from hashlib import md5
from lxml import etree
from bs4 import BeautifulSoup
import re
from multiprocessing.pool import Pool


def get_page(offset):
    global headers
    headers = {
        'cookie': 'ttcid=63fdd754f6774642862827170997465033; csrftoken=1dd771acffce13fff5deb0f904fe897f; tt_webid=6937591667655542309; s_v_web_id=verify_km1ucoaf_b8cM2YwH_D6vZ_4eQ7_BPxU_hjqFG1ZoNWRE; csrftoken=1dd771acffce13fff5deb0f904fe897f; tt_webid=6937591667655542309; __ac_signature=_02B4Z6wo00f01K5TTqgAAIDDZu-Htd0-wryud0oAAEvhfqsgqMAL.cEMjm9jCPksnhq6pTDblgbg3K8APL3wV8dPzhT9jiMZTL8UZEzHMj7hI-GjRon57EAvY7SPdW1h4zdgW.EoGndJTDqT8b; MONITOR_WEB_ID=534da03b-7a32-4de1-b0e3-9592a863e231; tt_scid=jAUhENFrFgvzH4O3sgBhvG0uS8BUwM7ZAZSw1uI2t7OW8NdElLnL6ZYRbbO.haz40a6e; __tasessionId=t5rh7t77d1615361020574',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 Edg/81.0.416.68',
        'referer': 'https://www.toutiao.com/search/?keyword=%E7%BE%8E%E5%A5%B3',
        'x-requested-with': 'XMLHttpRequest'
    }  # 头信息 加入参数
    params = {
        'aid': ' 24',
        'app_name': ' web_search',
        'offset': offset,
        'format': ' json',
        'keyword': ' 美女',
        'autoload': ' true',
        'count': ' 20',
        'en_qc': ' 1',
        'cur_tab': ' 1',
        'from': ' search_tab',
        'pd': ' synthesis',
        'timestamp': int(time.time())
    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)  # 构造url
    url = url.replace('=+', '=')  # 网址根本不一样
    # print(url)
    try:
        r = requests.get(url, headers=headers, params=params)
        r.content.decode('utf-8')
        if r.status_code == 200:
            return r.json()  # 返回json格式 因为全是字典类型
    except requests.ConnectionError as e:
        print(e)


def get_image(json):  # 获取图片
    if json.get('data'):  # 如果这个存在
        for item in json.get('data'):
            if item.get('title') is None:
                continue  # 如果标题是空值
            title = item.get('title')  # 获取标题
            # if item.get('image_list') is None:  # 进行判空
            #     continue
            # urls = item.get('image_list')  # 获得图片网址
            # for url in urls:  # 遍历这个urls
            #     url = url.get('url')
            #     # 使用正则拼接网址
            #     url = 'http://p1.pstatp.com/origin/' + 'pgc-image/' + url.split('/')[-1]
            if item.get('article_url') == None:
                continue
            url_page = item.get('article_url')
            # print(url_page)
            rr = requests.get(url_page, headers=headers)

            if rr.status_code == 200:
                pat = '<script>var BASE_DATA = .*?articleInfo:.*?content:(.*?)groupId.*?;</script>'
                match = re.search(pat, rr.text, re.S)
                if match != None:
                    result = re.findall(r'img src&#x3D;\\&quot;(.*?)\\&quot;', match.group(), re.S)
                    # for i in result:
                    #     print(i.encode('utf-8').decode('unicode_escape')
                    # 转换编码方式 把\u之类的改掉
                    yield {
                        'title': title,
                        'image': result
                    }
            #  格式出错，这里产生了十六进制的数值， 网址获取不了，明天看
            # yield {
            #     'title': title,
            #     'image': url
            # }  # 返回标题和网址


def save_image(content):
    path = 'E://Crawling//toutiao'  # 目录
    if not os.path.exists(path):  # 创建目录
        os.mkdir(path)
        os.chdir(path)
    else:
        os.chdir(path)
    # ------------------------------------------

    if not os.path.exists(content['title']):  # 创建单个文件夹
        if '\t' in content['title']:  # 以title为标题创建单个文件夹
            title = content['title'].replace('\t', '')  # 去除特殊符号 不然创建不了文件名称
            os.mkdir(title + '//')
            os.chdir(title + '//')
            print(title)
        else:
            title = content['title']
            os.mkdir(title + '//')  # 创建文件夹
            os.chdir(title + '//')
            print(title)
    else:  # 如果存在
        if '\t' in content['title']:  # 以title为标题创建单个文件夹
            title = content['title'].replace('\t', '')  # 去除特殊符号 不然创建不了文件名称
            os.chdir(title + '//')
            print(title)
        else:
            title = content['title']
            os.chdir(title + '//')
            print(title)
    for q, u in enumerate(content['image']):  # 遍历图片地址列表
        u = u.encode('utf-8').decode('unicode_escape')

        # 先编码在解码 获得需要的网址链接
        #  开始下载
        r = requests.get(u, headers=headers)
        if r.status_code == 200:
            # file_path = r'{0}/{1}.{2}'.format('美女', q, 'jpg')  # 文件的名字和地址，用三目运算符来调试文件夹的名字
            # hexdisgest() 返回十六进制图片
            with open(str(q) + '.jpg', 'wb') as fw:
                fw.write(r.content)
                print(f'该系列----->下载{q}张')


def main(offset):
    json = get_page(offset)
    get_image(json)
    for content in get_image(json):
        try:
            # print(content)
            save_image(content)
        except FileExistsError and OSError:
            print('创建文件格式错误，包含特殊字符串:')
            continue


if __name__ == '__main__':
    pool = Pool()
    groups = [j * 20 for j in range(8)]
    pool.map(main, groups) # 传offset偏移量
    pool.close()
    pool.join()