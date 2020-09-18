import requests
import json
import os
import re
from pyquery import PyQuery as pq


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}


# 获取 html 数据
def get_html(url):
    print("======正在获取第{}页数据======".format(page))
    resp = requests.get(url, headers=headers)
    html = resp.text
    data = json.loads(html)
    return data


#  获取 视频的真实播放地址  和  名字
def get_dowmurl(data):
    mess = data['data']['response']['list']
    intab = '?*/\|.:"><'
    for li in mess:
        mp4_name = li['title']
        for s in intab:
            if s in mp4_name:
                mp4_name = mp4_name.replace(s, '')
        mp4_url = li['url']
        a = requests.get(mp4_url)
        aa = a.text
        try:
            video = re.findall('<video class="video" src=(.*?)>', aa)[0].split('?')[0]
        except:
            print('error')
        print(video)
        yield mp4_name, video


#  保存视频
def save_mp4(mp4_name, mp4_url):
    print("正在保存: {}".format(mp4_name))
    path = r'E:\Users'
    if not os.path.exists(path):
        os.mkdir(path)
    path_d = path + '\{}.mp4'.format(mp4_name)
    a = requests.get(mp4_url, headers=headers).content
    with open(path_d, 'wb')as f:
        f.write(a)


# 主函数
def main(page):
    n = page * 20
    url = 'https://haokan.baidu.com/videoui/page/search?pn={}&rn=10&_format=json&tab=video&query=%E6%8A%BD%E7%83%9F'.format(n)
    data = get_html(url)
    mp4_mess = get_dowmurl(data)
    for mp4_name, mp4_url in mp4_mess:
        save_mp4(mp4_name, mp4_url)


if __name__ == '__main__':
    for page in range(1, 100):
        main(page)
