import sys
import requests
import re
import time
import os

time1=time.time()
# main_url = 'http://video.eastday.com/a/170612170956054127565.html'
main_url = 'https://video.eastday.com/a/200924073704576483221.html'
resp = requests.get(main_url)
#没有这行，打印的结果中文是乱码
resp.encoding = 'utf-8'
html = resp.text
link = re.findall(r'var mp4 = "(.*?)";', html)[0]
print(link)
link = 'https:'+link
dest_resp = requests.get(link)
#视频是二进制数据流，content就是为了获取二进制数据的方法
data = dest_resp.content
#保存数据的路径及文件名
path = 'E:\qw.mp4'

f = open(path, 'wb')
f.write(data)
f.close()
time2 = time.time()
print(u'ok,下载完成!')
print(u'总共耗时：' + str(time2 - time1))