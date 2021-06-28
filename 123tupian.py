import requests
from bs4 import BeautifulSoup
import urllib.request
import os
import random


n = 1


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

for i in range(1, 15):
    mainPage = 'https://www.123rf.com.cn/browse/search.php?keyword=%E9%AB%98%E7%A9%BA%E4%BD%9C%E4%B8%9A&mediaType=0&page=' + str(i)
    if i == 1:
        mainPage = 'https://www.123rf.com.cn/browse/search.php?keyword=%E9%AB%98%E7%A9%BA%E4%BD%9C%E4%B8%9A&mediaType=0&page=1'

    r = requests.get(mainPage)
    src = r.text
    soup = BeautifulSoup(src, 'lxml')

    for soup_new in soup.select('img'):
        print(soup_new)

        # for jpg_list in soup_new.a:
        #     imgurl = jpg_list.get("src")
        #
        #     try:
        #         finalpage = urllib.request.urlopen(imgurl)
        #         itdata = finalpage.read()
        #     except:
        #         continue
        #
        #     path = r'E:\Crawling\tiantan2'
        #     if not os.path.exists(path):
        #         os.mkdir(path)
        #     imggname = path + '\gaokong_' + str(n) + '.jpg'
        #
        #     print(imggname)
        #
        #     if os.path.exists(imggname) == True:
        #         n += 1
        #         print('allready in the fire')
        #         continue
        #     else:
        #         f = open(imggname, "wb")
        #         n += 1
        #         try:
        #             f.write(itdata)
        #         except:
        #             print("error")
        #
        #         f.close()
        #         print(imggname + ' ok!')