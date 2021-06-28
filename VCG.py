import urllib.request
import re
import os
import random
import requests
import json

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

my_headers = [
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7',
    'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 '

]
cou = 1
for i in range(1, 101):
    url = 'https://www.vcg.com/api/common/searchAllImage?page='+ str(i) + '&phrase=%E6%88%B4%E5%A4%B4%E7%9B%94%E9%AA%91%E8%BD%A6'
    data = requests.get(url, headers=header).json()
    imgurl = data['list']
    for x in imgurl:
        try:
            imgurll = 'https:' + x['url800']
        except:
            print('not url800')
        opener = urllib.request.build_opener()
        opener.addheaders = random.choice(my_headers)
        try:
            req = urllib.request.urlopen(imgurll)
        except:
            print("error")
        data = req.read()
        file_path = r'E:\Crawling\vcg\戴头盔骑车'
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        outputpath = file_path + '\\anquantouk_vcg_0001_' + str(cou) + '.jpg'
        if os.path.exists(outputpath):
            print('image already exit')
            cou += 1
            continue
        f = open(outputpath, 'wb')
        f.write(data)
        print(outputpath)
        f.close
        cou += 1
