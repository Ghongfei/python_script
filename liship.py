import requests
import re
import os
import urllib.request


#下载视频
def download():
    #获取网页源代码
    url="https://www.pearvideo.com/search.jsp?start=0&k=%E6%8E%A5%E5%B0%8F%E5%AD%A9"
    #模拟浏览器去请求服务器
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    }
    #状态码
    html=requests.get(url,headers=headers)
    print(url)

    #获取视频id   .*？匹配所有
    reg='<a href="(.*?)" class="actplay">'
    video_id=re.findall(reg,html.text)
    print(video_id)
    #拼接URL地址
    video_url=[]#接收拼接好的url
    starturl='http://www.pearvideo.com'+''
    for vid in video_id:
        newurl=starturl+'/'+vid
        video_url.append(newurl)
        #获取视频播放地址
        for purl in video_url:
            html=requests.get(purl,headers=headers)
            reg='srcUrl="(.*?)"'
            playurl=re.findall(reg,html.text)
            #获取视频标题
            reg='<h1 class="video-tt">(.*?)</h1>'
            video_name=re.findall(reg,html.text)
            #下载视频
            print('正在下载视频%s'%video_name)
            path='E:\\video'
            if not os.path.exists(path):
                os.mkdir(path)
            filepath=path+"/%s"%video_name[0]+'.mp4'
            #下载
            urllib.request.urlretrieve(playurl[0],filepath)

download()
