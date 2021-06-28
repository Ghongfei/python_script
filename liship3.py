import requests
import re
import os
import urllib.request
import time
import random


# 下载视频
def download():
    # 获取网页源代码
    # url="https://www.pearvideo.com/search.jsp?start=0&k=%E6%8E%A5%E5%B0%8F%E5%AD%A9"
    # 模拟浏览器去请求服务器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    }

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

    # #状态码
    # html=requests.get(url,headers=headers)
    f = open('html1.txt', 'r', encoding='UTF-8')
    data = f.read()
    f.close()

    # 获取视频id   .*？匹配所有
    reg = '<a href="(.*?)" class="actplay" target="_blank">'
    video_id = re.findall(reg, data)

    # 拼接URL地址
    video_url = []  # 接收拼接好的url
    starturl = 'http://www.pearvideo.com' + ''
    for vid in video_id:
        newurl = starturl + '/' + vid
        video_url.append(newurl)

        # 获取视频播放地址
    for purl in video_url:

        # html = requests.get(purl, headers=headers)
        html = requests.get(purl, headers={'User-Agent': random.choice(my_headers)})
        print(purl)
        reg_1 = '<video src="(.*?)"></video>'
        print(html.text)
        playurl = re.findall(reg_1, html.text)
        print(playurl)

        # 获取视频标题
        reg = '<h1 class="video-tt">(.*?)</h1>'
        video_name = re.findall(reg, html.text)

        intab = '?*/\|.:"><'
        for s in intab:
            if s in video_name[0]:
                video_name[0] = video_name[0].replace(s, '')

        # 下载视频
        print('正在下载视频%s' % video_name)
        path = r'E:\liship'
        if not os.path.exists(path):
            os.mkdir(path)
        filepath = path + "\%s" % video_name[0] + '.mp4'
        # 下载
        try:
            urllib.request.urlretrieve(playurl[0], filepath)
        except Exception:
            continue
        finally:
            # 休息数秒，预防IP被禁
            time.sleep(random.randint(0, 5) + random.random())


download()
