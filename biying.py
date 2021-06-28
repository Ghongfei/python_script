import time
import os
import re

import urllib
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

from header import utl_header



header = {
    'User-Agent': utl_header.get_header()
}
url = "https://cn.bing.com/images/async?q={0}&first={1}&count={2}&scenario=ImageBasicHover&datsrc=N_I&layout=ColumnBased" \
      "&mmasync=1&dgState=c*9_y*2226s2180s2072s2043s2292s2295s2079s2203s2094_i*71_w*198&IG=0D6AD6CBAF43430EA716510A4754C951&SFX={3}&iid=images.5599"

name = "戴头盔骑车"
path_b = "E:\\Crawling\\biying\\"

if not os.path.exists(path_b):
    os.mkdir(path_b)

path =  path_b + name


# 获取缩略图列表页
def getStartHtml(url, key, first, loadNum, sfx):
    page = urllib.request.Request(url.format(key, first, loadNum, sfx), headers=header)
    html = urllib.request.urlopen(page)
    return html


# 从缩略图列表页中找到原图的url，并返回这一页的图片数量
def findImgUrlFromHtml(html, rule, url, key, first, loadNum, sfx, count):
    soup = BeautifulSoup(html, "lxml")
    link_list = soup.find_all("a", class_="iusc")
    url = []
    for link in link_list:
        result = re.search(rule, str(link))

        # 将字符串"amp;"删除
        url = result.group(0)

        # 组装完整url
        url = url[8:len(url)]

        # 打开高清图片网址
        getImage(url, count)
        count += 1

    # 完成一页，继续加载下一页
    return count


# 从原图url中将原图保存到本地
def getImage(url, count):
    try:
        time.sleep(0.5)
        urllib.request.urlretrieve(url, path + '\\' + "anquantouk_by_2_" + str(count + 1) + '.jpg')
    except Exception:
        time.sleep(1)
        print("产生了一点点错误，跳过...")
    else:
        print("图片+1,成功保存 " + str(count + 1) + " 张图")


def main():
    key = urllib.parse.quote(name)
    first = 1
    loadNum = 35
    sfx = 1
    count = 0
    # 正则表达式
    rule = re.compile(r"\"murl\"\:\"http\S[^\"]+")

    if not os.path.exists(path):
        os.makedirs(path)
    while count < 500:
        html = getStartHtml(url, key, first, loadNum, sfx)
        count = findImgUrlFromHtml(html, rule, url, key, first, loadNum, sfx, count)
        first = count + 1
        sfx += 1


if __name__ == '__main__':
    main()
