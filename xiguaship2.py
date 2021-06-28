import you_get
import os
import urllib.request
from bs4 import BeautifulSoup
import time
import random
import multiprocessing

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

def getMp4(urlList):
    cmd_list = []
    for url in urlList:
        path_a = r"E:\tenxun"
        if not os.path.exists(path_a):
            os.mkdir(path_a)
        path = path_a + '\舞刀'
        if not os.path.exists(path):
            os.mkdir(path)
        cmds = 'you-get -o %s %s' % (path, url)
        cmd_list.append(cmds)
    for count, each in enumerate(cmd_list):
        print("正在下载第%s个视频，一共有%s个视频" % (count + 1, len(cmd_list)))
        os.system(each)


def make_page():
    for p in range(1, 21):
        if p % 8 == 0:
            time.sleep(random.random() * 3)
        'https://www.ixigua.com/search/舞刀/?logTag=nnk6CSnXGt__d4Y0ss867&keyword=%25E8%2588%259E%25E5%2588%2580'
        url = 'https://v.qq.com/x/search/?ses=qid%3DOldq7qgBL_MG0d_dDHpy4WB2lroOHciF_I2ZqDq_Rpu22oC_Ex0yYA%26last_query%3D%E6%8B%BF%E5%88%80%E7%A0%8D%E4%BA%BA%26tabid_list%3D0%7C1%7C11%7C2%7C3%7C4%7C6%7C12%7C21%7C14%7C5%7C17%7C8%7C10%7C13%7C15%7C20%7C7%26tabname_list%3D%E5%85%A8%E9%83%A8%7C%E7%94%B5%E5%BD%B1%7C%E6%96%B0%E9%97%BB%7C%E7%94%B5%E8%A7%86%E5%89%A7%7C%E7%BB%BC%E8%89%BA%7C%E5%8A%A8%E6%BC%AB%7C%E7%BA%AA%E5%BD%95%E7%89%87%7C%E5%A8%B1%E4%B9%90%7C%E6%B1%BD%E8%BD%A6%7C%E4%BD%93%E8%82%B2%7C%E9%9F%B3%E4%B9%90%7C%E6%B8%B8%E6%88%8F%7C%E5%8E%9F%E5%88%9B%7C%E6%8B%8D%E5%AE%A2%7C%E8%B4%A2%E7%BB%8F%7C%E6%95%99%E8%82%B2%7C%E6%AF%8D%E5%A9%B4%7C%E5%85%B6%E4%BB%96%26resolution_tabid_list%3D0%7C1%7C2%7C3%7C4%7C5%26resolution_tabname_list%3D%E5%85%A8%E9%83%A8%7C%E6%A0%87%E6%B8%85%7C%E9%AB%98%E6%B8%85%7C%E8%B6%85%E6%B8%85%7C%E8%93%9D%E5%85%89%7CVR&q=%E6%8B%BF%E5%88%80%E7%A0%8D%E4%BA%BA&needCorrect=%E6%8B%BF%E5%88%80%E7%A0%8D%E4%BA%BA&stag=3&cur=' + str(p) + '&cxt=tabid%3D0%26sort%3D0%26pubfilter%3D0%26duration%3D0'
        if p == 1:
            url = "https://v.qq.com/x/search/?ses=qid%3DOldq7qgBL_MG0d_dDHpy4WB2lroOHciF_I2ZqDq_Rpu22oC_Ex0yYA%26last_query%3D%E6%8B%BF%E5%88%80%E7%A0%8D%E4%BA%BA%26tabid_list%3D0%7C1%7C11%7C2%7C3%7C4%7C6%7C12%7C21%7C14%7C5%7C17%7C8%7C10%7C13%7C15%7C20%7C7%26tabname_list%3D%E5%85%A8%E9%83%A8%7C%E7%94%B5%E5%BD%B1%7C%E6%96%B0%E9%97%BB%7C%E7%94%B5%E8%A7%86%E5%89%A7%7C%E7%BB%BC%E8%89%BA%7C%E5%8A%A8%E6%BC%AB%7C%E7%BA%AA%E5%BD%95%E7%89%87%7C%E5%A8%B1%E4%B9%90%7C%E6%B1%BD%E8%BD%A6%7C%E4%BD%93%E8%82%B2%7C%E9%9F%B3%E4%B9%90%7C%E6%B8%B8%E6%88%8F%7C%E5%8E%9F%E5%88%9B%7C%E6%8B%8D%E5%AE%A2%7C%E8%B4%A2%E7%BB%8F%7C%E6%95%99%E8%82%B2%7C%E6%AF%8D%E5%A9%B4%7C%E5%85%B6%E4%BB%96%26resolution_tabid_list%3D0%7C1%7C2%7C3%7C4%7C5%26resolution_tabname_list%3D%E5%85%A8%E9%83%A8%7C%E6%A0%87%E6%B8%85%7C%E9%AB%98%E6%B8%85%7C%E8%B6%85%E6%B8%85%7C%E8%93%9D%E5%85%89%7CVR&q=%E6%8B%BF%E5%88%80%E7%A0%8D%E4%BA%BA&needCorrect=%E6%8B%BF%E5%88%80%E7%A0%8D%E4%BA%BA&stag=3&cur=1&cxt=tabid%3D0%26sort%3D0%26pubfilter%3D0%26duration%3D0"
        req = urllib.request.Request(url, headers={'User-Agent': random.choice(my_headers)})
        page = urllib.request.urlopen(req)
        data = page.read()
        data = data.decode('utf-8','ignore')
        soup = BeautifulSoup(data,features="lxml")
        for link in soup.select('.result_item'):
            ahref = link.a['href']
            urlList.append(ahref)


if __name__ == '__main__':
    po = multiprocessing.Pool(51)
    num = 0
    urll = []
    print('正在获取视频链接')
    make_page()
    print(urlList)
    getMp4(urlList)
