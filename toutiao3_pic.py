import requests
from bs4 import BeautifulSoup
from skimage import io
import urllib
import re
import time
import json
import os
import sys

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    , 'Accept': 'application/json, text/javascript'
    , 'Host': 'www.toutiao.com'
    , 'Connection': 'keep-alive'
    , 'Accept-Encoding': 'gzip, deflate'
    , 'Accept-Language': 'zh-CN,zh;q=0.8'
    , 'Upgrade-Insecure-Requests': '1'
    , 'Referer': 'http://www.toutiao.com/search/'
}

url = 'http://www.toutiao.com/search_content/?offset={}&format=json&keyword={}&autoload=true&count=20&cur_tab=3'
# urltest = 'http://www.toutiao.com/search_content/?offset=0&format=json&keyword=fate&autoload=true&count=20&cur_tab=3'

urllist = []  # 创建个列表用于存放每次异步加载所更新出来的20条网页url

name = input('请输入所要查找的图片关键词')
for i in range(0, 10):  # 爬取前100条链接
    urllist.append(url.format(i, name))

path = r'E:\picture'


def Schedule(a, b, c):  # 显示下载进度
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    sys.stdout.write('\r%.2f%%' % per)
    time.sleep(1)
    if per == 100:
        print('该图片加载完成')


urlname = []  # 存放每个图集的名称
urllist2 = []  # 存放每个图集的链接


def get_link(url):
    session = requests.Session()
    res = session.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    jd = json.loads(soup.text)
    for articleurl in jd['data']:
        name = articleurl['title']
        urlimg = articleurl['url']

        urlname.append(name)
        urllist2.append(urlimg)
        # print('图集名称:\n',name,'\n图集链接:\n',url)
    return urllist2


# print(urllist)
for url in urllist:
    # print('父URL',url)
    get_link(url)
    time.sleep(1)


def img_save(urllist3, urlname):
    i2 = 1
    for imgurl, imgname in zip(urllist3, urlname):  # 将列表中所存放的图片url打印出来，通过skimage将图片打印到控制台上
        print('图片', i2, '链接:', imgurl)
        print('图片', i2, '预览:\n')
        imgname2 = imgname.lstrip('origin/')
        try:  # 查看图片

            fateimg = io.imread(imgurl)
            io.imshow(fateimg)
            io.show()
        except OSError:
            print('图片打开失败！！')
        try:  # 保存图片
            if not os.path.exists(path):  # 若该路径下面的文件夹不存在则创建一个
                os.mkdir(path)

            urllib.request.urlretrieve(imgurl, path + '\\' + 'fate系列' + imgname2 + '%s.jpg' % i2, Schedule)

            print('下载完成\n\n')
        except Exception:
            print('下载失败')
        # time.sleep(1)
        i2 += 1


# 通过正则表达式以及json将每张图片的url爬取出来并打印并下载到本地文件夹
def get_jsonurl(url, urlnamecon):
    urllist3 = []  # 该列表用于存放每张图片的url
    urlname = []
    res = requests.session.get(url, headers=headers)
    res.text
    soup = BeautifulSoup(res.text, 'html.parser')

    message = re.findall('gallery: (.*?),\n', soup.text, re.S)  # 通过正则表达式将json文件提取出来
    jd = json.loads(message[0])  # 通过loads方法将json文件转化为字典形式
    url = jd['sub_images']  # 通过json在线解析器将解析出来的字典类型的网页元素通过键找出其所对应的值
    for url1 in url:
        urllist3.append(url1['url'])
        urlname.append(url1['uri'])  # 将每张图片的名称保存到列表中
    img_save(urllist3, urlname)


num = 1
for urlcontent, urlnamecon in zip(urllist2, urlname):
    print('图集', num, '名称:', urlnamecon)  # 打印每个图集的名称
    print('图集', num, '链接:', urlcontent)  # 打印每个图集的链接
    print(len(urlname))
    get_jsonurl(urlcontent, urlnamecon)
    num += 1
