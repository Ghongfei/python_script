import re
import requests
import os

f = open('html.txt', 'r')
data = f.read()
f.close()
new_list = []
time = 0

'''
response = requests.get('https://haokan.baidu.com/videoui/page/search?query=%E6%89%93%E6%9E%B6%E8%A7%86%E9%A2%91')
data = line.text
'''

url = re.findall('<a href="(.*?)" class="list-container videolist clearfix" target="_blank">', data)
for a in url:  # type str
    if a.startswith('ht'):
        new_list.append(a)


for url_1 in new_list:
    response_1 = requests.get(url_1)
    data_1 = response_1.text
    print(data_1)
    video = re.findall('<video class="video" src=(.*?)>', data_1)[0]
    title = re.findall('<h2 class="videoinfo-title">(.*?)</h2>', data_1)[0]
    name = f'{title}.mp4'
    video_response = requests.get(video)
    video_3 = video_response.content
    path = r'E:\\工地人干活'
    if not os.path.exists(path):
        os.mkdir(path)
    with open(path + '\{name}', 'wb') as fw:
        fw.write(video_3)
        fw.flush()
        time += 1
        print(f'已经爬取{time}个视频')
