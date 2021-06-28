import time
import random
import socket
import requests
import json
import urllib
import os

# 设置请求超时时间，防止长时间停留在同一个请求
socket.setdefaulttimeout(20)


def pullImgfFromSoGou(category, num, path):
    count = 0

    for i in range(num//48):
        n = i + 1
        url = 'https://pic.sogou.com/napi/pc/searchList?mode=1&start='+str(n*48)+'&xml_len=48&query='+category
        imgs = requests.get(url)
        jd = json.loads(imgs.text)
        jd = jd['data']['items']
        imgs_url = []
        for j in jd:
            imgs_url.append(j['picUrl'])
        for img_url in imgs_url:
            print(' '+str(count)+'.jpg '+' Downloading...')
            try:
                urllib.request.urlretrieve(img_url, path + '\\' + "anquantouk_sg_4_" + str(count) + '.jpg')
            # 请求时可能会出现404HttpError，或者连接重置等等异常导致程序突出，这里直接采用Exception进行处理，出现了异常只需要跳过进行下一张的下载即可
            except Exception:
                continue
            finally:
                count += 1
                # 休息数秒，预防IP被禁
                time.sleep(random.randint(0, 1)+random.random())
            # 每批次下载完成多休息几秒
            time.sleep(random.randint(0,1))
    print('Download complete!')


if __name__ == '__main__':
    path = 'E:\\Crawling\\sougou'
    if not os.path.exists(path):
        os.mkdir(path)
    name = '电动车头盔'
    path_a = path + '\\' + name
    if not os.path.exists(path_a):
        os.mkdir(path_a)
    pullImgfFromSoGou(name, 2000, path_a)

