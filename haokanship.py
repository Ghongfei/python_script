# import sys
# import re, os
# import requests
# import random
# from you_get import common as you_get
# import urllib.request
# import json
#
# my_headers = [
#     'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
#     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
#     'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)',
#     'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
#     'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
#     'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
#     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
#     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7',
#     'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ',
#     'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.34 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.34'
# ]
#
#
# def getVideo(url, path, my_headers):
#     req = urllib.request.Request(url, headers={'User-Agent': random.choice(my_headers)})
#     page = urllib.request.urlopen(req)
#     data = page.read()
#     data = data.decode('utf-8', 'ignore')
#     data_json = json.loads(data)
#
#     videolists = data_json['data']['response']['list']
#
#     cmd_list = []
#
#     for v in videolists:
#         video_url = v['url']
#         print(video_url)
#
#         # try:
#         #     cmds = 'you-get -o %s %s' % (path, video_url)
#         #     cmd_list.append(cmds)
#         #     for each in enumerate(cmd_list):
#         #         os.system(each)
#         # except:
#         #     print("error")
#
#         try:
#             sys.argv = ['you_get', '-o', path, video_url]  # 视频的属性编辑，选择路径等
#             you_get.main()  # 开始下载
#             print('下载完成!')
#         except:
#             print('下载失败!')
#
#
# if __name__ == '__main__':
#
#     for i in range(1, 1000):
#         url = 'http://haokan.baidu.com/videoui/page/search?pn=' + str(i) + '&rn=10&_format=json&tab=video&query=%E6%89%8B%E6%8B%BF%E6%88%98%E5%88%80'
#
#     path = r'E:\haokan'
#     getVideo(url, path, my_headers)



import sys
import re,os
import requests
from you_get import common as you_get

def getVideo(url,path,headers):
    demo = requests.get(url,headers=headers)# 获取网站信息
    data = demo.json()# 转换为JSON格式
    data_list = data['data']['response']['videos']# 获取每个视频的属性列表

    # 遍历，将每一个视频信息展示出来
    for i in data_list:
        title = i['title'] + '.mp4'# 获取视频名称(描述)，视频要修改为的名称，为后边改名做准备
        url1 = i['play_url']# 获取视频源url
        videoName = re.split('\?|/',url1)[5][:80]+'.mp4'# 视频下载后，会是一大串字母和数字的组合，这个主要就是获取视频下载后的原名称

        # 开始下载
        print('开始下载：' + title)
        try:
            sys.argv = ['you_get', '-o',path,url1]# 视频的属性编辑，选择路径等
            you_get.main()# 开始下载
            print('👆下载完成')
            os.rename(path + videoName, path + title)# 下载完成后，改名操作
        except:
            print(title + '下载失败!')
if __name__ == '__main__':
    url = 'https://haokan.baidu.com/videoui/api/videorec?tab=yingshi&act=pcFeed&pd=pc&num=20&shuaxin_id=1592551368953'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36 Edg/83.0.478.54',
        'cookie': 'BIDUPSID=517516CBF0261FA0AF6B039EAFEDF39C; PSTM=1589624436; BAIDUID=517516CBF0261FA090A0395C8BF0F31A:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PC_TAB_LOG=haokan_website_page; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1592530622,1592545903; H_PS_PSSID=31906_1444_31671_21118_31254_32045_30823_32111; delPer=0; PSINO=2; yjs_js_security_passport=d270bf2526b634428ea81932e213c285b8e7cf21_1592546748_js; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1592550475; reptileData=%7B%22data%22%3A%22e3b78a008f54876b4fc19fe55faea5fb1ae054d9580474b00db252837ba6a6554cbfde0ada4567b9cad2322c5d972031cb300664e248e8f4a7b27fd91a479f4e02a1e7eceffa642289eba12075334687515e1451aa72eced7ac42e3fbb88a87139c95727da119f5dd9b85d281d98d4d98b943f43a06c3f13e6b63b812c5c40ce%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%2243b164d6%22%7D'}
    path = r'E:\haokan\\'

    getVideo(url,path,headers)