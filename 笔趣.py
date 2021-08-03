import requests, sys
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
}


# if __name__ == '__main__':
#     first_url = 'http://www.biqukan.com/'
#     url = "http://www.biqukan.com/1_1094/"
#     req = requests.get(url, headers=header)
#     req.encoding = 'gbk'
#     if req.status_code != 200:
#         print("status_code:错误")
#     html = req.text
#     bf = BeautifulSoup(html, 'html.parser')
#     divs = bf.find_all('div', class_='listmain')
#     a_bf = BeautifulSoup(str(divs[0]), 'html.parser')
#     a_list = a_bf.find_all('a')
#     for a in a_list:
#         print(a.string, first_url + a.get('href'))


class downloader(object):

    # 初始化
    def __init__(self):
        self.text_url = 'http://www.biqukan.com/1_1094/'
        # 存放章节名
        self.name = []
        # 存放章节链接
        self.urls = []
        # 章节数
        self.nums = 0

    # 获取下载链接
    def get_download_url(self):
        req = requests.get(self.text_url, headers=header)
        req.encoding = 'gbk'
        html = req.text
        div_bf = BeautifulSoup(html, 'html.parser')
        div = div_bf.find_all('div', class_='listmain')
        a_bf = BeautifulSoup(str(div[0]), 'html.parser')
        a_list = a_bf.find_all('a')

        # 剔除不必要的章节，并统计章节数
        self.nums = len(a_list[13:])
        for a in a_list:
            self.name.append(a.string)
            self.urls.append(self.text_url.split('1_1094')[0] + a.get('href'))

    # 获取下载内容
    def get_contents(self, url):
        req = requests.get(url, headers=header)
        req.encoding = 'gbk'
        html = req.text
        bf = BeautifulSoup(html, 'html.parser')
        texts = bf.find_all('div', class_='showtxt')
        texts = texts[0].text.replace('\xa0' * 8, '\n')
        return texts

    # 保存
    def writer(self, name, path, text):
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n')



if __name__ == '__main__':
    d = downloader()
    d.get_download_url()
    print('开始下载...')
    for i in range(d.nums):
        d.writer(d.name[i], '一念永恒.txt', d.get_contents(d.urls[i]))
    print('下载完成')






# -*- coding:UTF-8 -*-
# from bs4 import BeautifulSoup
# import requests, sys
# import time
# import random
#
# class downloader(object):
#
#
#     def __init__(self):
#         self.server = 'http://www.biqukan.com/'
#         self.target = 'http://www.biqukan.com/1_1094/'
#         self.names = []
#         self.urls = []
#         self.nums = 0
#         self.retry = 3
#
#
#     def get_download_url(self):
#         req = requests.get(url = self.target)
#         html = req.text
#         div_bf = BeautifulSoup(html)
#         div = div_bf.find_all('div', class_ = 'listmain')[0].find_all('a')
#         self.nums = len(div[15:])
#         for each in div[15:]:
#             self.names.append(each.string)
#             self.urls.append(self.server + each.get('href'))
#
#
#     def get_contents(self, response):
#         if response:
#             bf=BeautifulSoup(response.text,"html.parser")
#             texts = bf.find_all('div', attrs={'id':'content'})
#             text = texts[0].text.replace('\xa0'*8,'\n\n')
#             return text
#         else:
#             return "Find None"
#
#
#     def writer(self, name, path, text):
#         write_flag = True
#         with open(path, 'a', encoding='utf-8') as f:
#             f.write(name + '\n')
#             f.writelines(text)
#             f.write('\n\n')
#
#
#     def call_target(url,downloader):
#         print(downloader.retry)
#         request_headers={}
#         request_headers['User-Agent']=get_random_useragent()
#         response = requests.get(url = url)
#         status_code =response.status_code
#         if status_code == 200:
#             downloader.retry = 3
#             return response
#         if status_code !=200 and downloader.retry > 0:
#             print(status_code)
#             print(downloader.retry)
#             downloader.retry-=1
#             time.sleep(random.randint(3,15))
#             return call_target(url, downloader)
#         else:
#             downloader.retry = 3
#             return None
#
#
#     def get_random_useragent():
#         user_agents=["Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0", "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)", "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1", "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"]
#         return user_agents[random.randint(0,len(user_agents)-1)]
#
#
# if __name__ == "__main__":
#     dl = downloader()
#     dl.get_download_url()
#     print('《一年永恒》开始下载：')
#     for i in range(dl.nums):
#         dl.writer(dl.names[i], '一念永恒.txt', dl.get_contents(dl.call_target(dl.urls[i],dl)))
#         sys.stdout.write(" 已下载:%.3f%%" % float(i/dl.nums) + '\r')
#         sys.stdout.flush() print('《一年永恒》下载完成')
