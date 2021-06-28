import you_get
import os
import urllib.request
from bs4 import BeautifulSoup
import time
import random


header = {'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
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
urlList = []
def getMp4(path,urlList):
    cmd_list = []
    for url in urlList:
        cmds = 'you-get -o %s --playlist %s'%(path,url)
        cmd_list.append(cmds)
    for count,each in enumerate(cmd_list):
        print("正在下载第%s个视频，一共有%s个视频"%(count+1,len(cmd_list)))
        os.system(each)
        
def make_page():
    for p in range(31,98):
        if p % 8 == 0:
            time.sleep(random.random()*3)

        url = "https://so.iqiyi.com/so/q_%E7%9B%91%E6%8E%A7%E6%8A%BD%E7%83%9F_ctg__t_0_page_{}_p_1_qc_0_rd__site__m_1_bitrate__af_0".format(str(p))
        # req = urllib.request.Request(url, headers=header)
        # page=urllib.request.urlopen(req)
        # data = page.read()
        # data = data.decode('utf-8','ignore')
        # soup = BeautifulSoup(data,features="lxml")
        # for link in soup.select('.video-item'):
        #     +links = 'https:'+ link.a['href']
        urlList.append(url)
if __name__ == '__main__':
    print('正在获取视频链接')
    make_page()
    path = "E:\Crawling\触电"
    if not os.path.exists(path):
        os.mkdir(path)
    print(urlList)
    getMp4(path,urlList)

