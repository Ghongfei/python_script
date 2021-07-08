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

f = open('../爬虫/梨视频.txt', encoding ="utf-8")
data = f.read()
video = re.findall('<a href="(.*?)" class="actplay" target="_blank">', data)

for i in range(len(video)):
    url = 'https://www.pearvideo.com/' + video[i]
    req1 = urllib.request.Request(url, headers={'User-Agent': random.choice(my_headers)})
    page1 = urllib.request.urlopen(req1)
    data1 = page1.read()
    data1 = data1.decode('utf-8', 'ignore')
    try:
        mp4v = re.findall('srcUrl="(.*?)",vdoUrl', data1)[0]
        title = re.findall('<title>(.*?)</title>', data1)[0][:-17]
    except:
        continue

    video_response = requests.get(mp4v)
    video_3 = video_response.content
    if os.path.exists("E:/打架视频3/%s.mp4" % title):
        print('error')
        continue
    else:
        try:
            with open("E:/打架视频3/%s.mp4" % title, 'wb') as fw:
                fw.write(video_3)
                print("%s.mp4" % title + "ok")
                fw.flush()
        except:
            continue

f.close()