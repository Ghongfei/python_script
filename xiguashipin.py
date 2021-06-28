# import requests
# import re
# import json
# import base64
#
# page_url = 'https://www.ixigua.com/i6717973108818444814/'
#
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
# headers = {
#     "User-Agent": user_agent
# }
# page_content = requests.get(page_url, headers=headers).content.decode(encoding='utf-8');
# # print(page_content)
#
# config_info = re.findall(r'window\.__pageState=.*\}</script>', page_content)[0]
# config_info = json.loads(config_info.split('window.__pageState=')[1].replace('</script>', ''))['video']
#
# title = config_info['title']
#
# v_sdk = 'https://vas.snssdk.com/video/openapi/v1/'
# params = {
#     'action': 'GetPlayInfo',
#     'video_id': config_info['vid'],
#     'nobase64': 'false',
#     'ptoken': config_info['businessToken'],
#     'vfrom': 'xgplayer'
# }
# v_header = {
#     'Authorization': config_info['authToken'],
#     "User-Agent": user_agent
# }
# video_info = json.loads(requests.get(v_sdk, params=params, headers=v_header).content.decode())
# if video_info['code'] == 0:
#     h_video = video_info['data']['video_list']['video_' + str(video_info['total'])]
#     v_type = h_video['vtype']
#     video_url = str(base64.urlsafe_b64decode(h_video['main_url']), encoding='utf-8')
#     print(title)
#     print(video_url)
#     with open('./%s.%s' % (title, v_type),'wb') as f:
#         f.write(requests.get(video_url).content)
#     print('下载成功！')
# else:
#     print('请求失败!')
#
#

from base64 import b64decode
from lxml import etree
import requests
import json
import re
import os


class XiGuaSpider:

    def __init__(self):
        self.headers = {
            'Referer': 'https://www.ixigua.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'cookie': 'wafid=5b014d14-4285-413a-9dac-80e467ad5b4e; wafid.sig=Coe4SV6gStmKvfg897vmEd6h4_k; ttwid=6827754753289045508; ttwid.sig=hZChEHZDh7I1GdyST_waUAu31MA; xiguavideopcwebid=6827754753289045508; xiguavideopcwebid.sig=PPinOOHLyRkB7vLZeARYw7faelQ; SLARDAR_WEB_ID=91892236-9025-4d06-9d8e-1ec85233c784; _ga=GA1.2.15757958.1589710551; ixigua-a-s=1; _gid=GA1.2.1010024108.1589876453; s_v_web_id=kadne2g1_M7vfty8L_ecKr_47jB_8GWc_ctMlrqAXOgQy; _gat_gtag_UA_138710293_1=1',
        }

        self.video_dirs = 'E:\\xiguaship'


    def download_file(self, file_path, download_url):
        print('*' * 100)
        print(f"保存路径：{file_path}")
        print(f'下载URL：{download_url}')
        response = requests.get(url=download_url, headers=self.headers, stream=True)
        content_size = int(response.headers["content-length"])  # 视频内容的总大小
        size = 0
        with open(file_path, "wb") as file:  # 非纯文本都以字节的方式写入
            for data in response.iter_content(chunk_size=1024):  # 循环写入
                file.write(data)  # 写入视频文件
                file.flush()  # 刷新缓存
                size += len(data)  # 叠加每次写入的大小
                # 打印下载进度
                print("\r文件下载进度:%d%%(%0.2fMB/%0.2fMB)" % (
                    float(size / content_size * 100), (size / 1024 / 1024),
                    (content_size / 1024 / 1024)),
                      end=" ")
        print()

    def get_response(self, url):
        response = None
        try:
            response = requests.get(url, headers=self.headers)
        except Exception as e:
            print(e)
        return response

    def parse_detail(self, url):
        response = self.get_response(url)
        if not response:
            return
        html = response.text
        document = etree.HTML(html)
        title = ''.join(document.xpath('//*[@class="hasSource"]/text()'))
        if not title:
            title = ''.join(document.xpath('//*[@class="teleplayPage__Description__header"]/h1/text()'))

        title = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "-", title)
        pattern = r'\<script.*?\>window\._SSR_HYDRATED_DATA=(.*?)\</script\>'
        result = re.findall(pattern, html)
        if len(result) < 1:
            print('没有找到下载链接。。。')
            return None
        result = result[0]
        data = json.loads(result)
        with open('video.json', 'w', encoding='utf-8') as f:
            json.dump(data, f)

        try:
            video_list = data['Projection']['video']['videoResource']['normal']['video_list']
        except Exception as e:
            print('异常信息：', e)
            video_list = data['Teleplay']['videoResource']['normal']['video_list']

        video_3 = video_list.get('video_3')
        if not video_3:
            video_3 = video_list.get('video_2')
        video_url = video_3['main_url']
        video_url = b64decode(video_url).decode('utf-8')

        if not os.path.exists(self.video_dirs):
            os.mkdir(self.video_dirs)
        file_path = f"{self.video_dirs}/{title}.mp4"
        self.download_file(file_path, video_url)

    def start_requests(self):
        url = 'https://www.ixigua.com/i6829205207210000909'
        self.parse_detail(url)

    def run(self):
        self.start_requests()


if __name__ == '__main__':
    XiGuaSpider().run()