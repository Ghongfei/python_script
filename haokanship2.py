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

for i in range(1, 1000):
    url = 'http://haokan.baidu.com/videoui/page/search?pn='+ str(i) +'&rn=10&_format=json&tab=video&query=%E9%AB%98%E7%A9%BA%E5%AE%89%E5%85%A8%E5%B8%A6'
    req = urllib.request.Request(url, headers={'User-Agent': random.choice(my_headers)})
    page = urllib.request.urlopen(req)
    data = page.read()
    data = data.decode('utf-8', 'ignore')
    data_json = json.loads(data)
    videolists = data_json['data']['response']['list']
    for v in videolists:
        video_url = v['url']
        print(video_url)
        v_list.append(video_url)
        req1 = urllib.request.Request(video_url, headers={'User-Agent': random.choice(my_headers)})
        page1 = urllib.request.urlopen(req1)
        data1 = page1.read()
        data2 = data1.decode('utf-8', 'ignore')
        try:
            video = re.findall('<video class="video" src=(.*?)>', data2)[0]
            title = re.findall('<h2 class="videoinfo-title">(.*?)</h2>', data2)[0]
        except:
            print('error')
            continue
        video_response = requests.get(video)
        video_3 = video_response.content
        path = r'E:\Crawling\haokanship\高空安全带'
        if not os.path.exists(path):
            os.mkdir(path)
        if os.path.exists(path + "\%s.mp4" % title):
            print('error')
            continue
        else:
            with open(path + "\%s.mp4" % title, 'wb') as fw:
                fw.write(video_3)
                print("%s.mp4" % title + "ok")
                fw.flush()