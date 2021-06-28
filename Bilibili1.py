import you_get
import os
import urllib.request
from bs4 import BeautifulSoup
import time
import random

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

urlList = []
def getMp4(path,urlList):
    cmd_list = []
    for url in urlList:
        cmds = 'you-get -o %s --format=flv %s'%(path,url)
        cmd_list.append(cmds)
    for count,each in enumerate(cmd_list):
        print("正在下载第%s个视频，一共有%s个视频"%(count+1,len(cmd_list)))
        os.system(each)
def make_page():
    for p in range(1,51):
        if p % 8 == 0:
            time.sleep(random.random()*3)

        url = "https://search.bilibili.com/all?keyword=%E5%88%80%E8%88%9E&page=" + str(p)
        req = urllib.request.Request(url, headers=header)
        page = urllib.request.urlopen(req)
        data = page.read()
        data = data.decode('utf-8','ignore')
        soup = BeautifulSoup(data,features="lxml")
        for link in soup.select('.video-item'):
            links = 'https:'+ link.a['href']
            urlList.append(links)
if __name__ == '__main__':
    print('正在获取视频链接')
    make_page()
    path = "E:\\Crawling\\bilibili\\刀舞"
    if not os.path.exists(path):
        os.mkdir(path)
    getMp4(path,urlList)
