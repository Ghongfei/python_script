import re
import requests
response_1 = requests.get("https://haokan.baidu.com/v?vid=16212487623005383436")
data_1 = response_1.text
video = re.findall('<video class="video" src=(.*?)>', data_1)[0]
title = re.findall('<h2 class="videoinfo-title">(.*?)</h2>', data_1)[0]

video_response = requests.get(video)

video_3 = video_response.content

with open('E:/安全帽/video/3.mp4', 'wb') as fw:
    fw.write(video_3)
    fw.flush()

