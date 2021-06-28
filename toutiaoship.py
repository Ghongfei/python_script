# import sys
# import requests
# import re
# import time
# import os
#
# time1=time.time()
# # main_url = 'http://video.eastday.com/a/170612170956054127565.html'
# main_url = 'https://video.eastday.com/a/200924073704576483221.html'
# resp = requests.get(main_url)
# #没有这行，打印的结果中文是乱码
# resp.encoding = 'utf-8'
# html = resp.text
# link = re.findall(r'var mp4 = "(.*?)";', html)[0]
# print(link)
# link = 'https:'+link
# dest_resp = requests.get(link)
# #视频是二进制数据流，content就是为了获取二进制数据的方法
# data = dest_resp.content
# #保存数据的路径及文件名
# path = 'E:\qw.mp4'
#
# f = open(path, 'wb')
# f.write(data)
# f.close()
# time2 = time.time()
# print(u'ok,下载完成!')
# print(u'总共耗时：' + str(time2 - time1))

import re
import urllib.request
import random
import json
import requests
import os

my_headers = [
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7',
    'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.34 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.34'
]
v_list = []

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }

count = 1

for page in range(1, 1000):

    url = 'https://quanmin.baidu.com/wise/growth/api/home/searchmorelist?rn=12&pn={}&q=%E9%AB%98%E7%A9%BA%E4%BD%9C%E4%B8%9A&type=search&_format=json'.format(page)
    response = requests.get(url=url, headers=headers)
    html_data = response.json()
    lis = html_data['data']['list']['video_list']
    for li in lis:
        play_url = li['play_url']

        path = r"E:\Crawling\quanming"
        if not os.path.exists(path):
            os.mkdir(path)

        filename = path + "\\" + "belt_quanming_0002_" + str(count) + '.mp4'
        response_2 = requests.get(url=play_url, headers=headers)

        with open(filename, mode='wb') as f:
            try:
                f.write(response_2.content)
            except:
                print('error')
            print("下载中：")
            print(play_url)

        count += 1
