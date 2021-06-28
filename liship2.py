import os
import requests
import re

# video存放文件的目录
path = r'E:\video'
# 判断目录是否存在 如果没有就创建
if not os.path.exists(path):
    os.mkdir(path)
ID = input('请输入梨视频的ID:')
url = 'https://www.pearvideo.com/video_' + ID
# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4208.400'
}

response = requests.get(url, headers=headers)
video_url = re.findall('srcUrl="(.*?.mp4)",vdoUrl=srcUrl', response.text)[-1]

# 名字的设置
name1 = input('给视频起一个名字吧：')
name2 = video_url.split('/')[-1]
name = name1 + name2

# 访问数据
data = requests.get(video_url)
# 下载文件
with open(path + '/' + name, mode='wb')as f:
    f.write(data.content)
print(name + '下载完成')

