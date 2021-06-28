# import requests
# import os
#
#
# def getManyPages(keyword,pages):
#     params=[]
#     for i in range(0,30*pages+30,30):
#         params.append({
#                       'tn': 'resultjson_com',
#                       'ipn': 'rj',
#                       'ct': 201326592,
#                       'is': '',
#                       'fp': 'result',
#                       'queryWord': keyword,
#                       'cl': 2,
#                       'lm': -1,
#                       'ie': 'utf-8',
#                       'oe': 'utf-8',
#                       'adpicid': '',
#                       'st': -1,
#                       'z': '',
#                       'ic': 0,
#                       'word': keyword,
#                       's': '',
#                       'se': '',
#                       'tab': '',
#                       'width': '',
#                       'height': '',
#                       'face': 0,
#                       'istype': 2,
#                       'qc': '',
#                       'nc': 1,
#                       'fr': '',
#                       'pn': i,
#                       'rn': 30,
#                       'gsm': '3c',
#                       '1488942260214': ''
#                   })
#     url = 'https://image.baidu.com/search/acjson'
#     urls = []
#     for i in params:
#         urls.append(requests.get(url,params=i).json().get('data'))
#
#     return urls
#
#
# def getImg(dataList, localPath):
#     # 新建文件夹
#     if not os.path.exists(localPath):
#         os.mkdir(localPath)
#
#     x = 0
#     for list in dataList:
#         for i in list:
#             if i.get('thumbURL') != None:
#                 print('正在下载：%s' % i.get('thumbURL'))
#                 ir = requests.get(i.get('thumbURL'))
#                 open(localPath + '%d.jpg' % x, 'wb').write(ir.content)
#                 x += 1
#             else:
#                 print('图片链接不存在')
#
# if __name__ == '__main__':
#     # 参数1:关键字，参数2:要下载的页数
#     dataList = getManyPages('人脸',20)
#     # 参数2:指定保存的路径
#     path = r'E:\人脸'
#     if not os.path.exists(path):
#         os.mkdir(path)
#     getImg(dataList, path)
#
#

'''
注释：
    @author is leilei
    百度图片爬虫，采用selenium模拟鼠标点击形式
    1. 将要搜索的文本表示成list
    2. 打开百度图片官网，输入文本，搜索
    3. 逐条下载对应的图片
注：
    本代码支持断点续爬！
'''

# import os
# import uuid
# import time
# import random
# import urllib
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys  # 键盘类
#
# def send_param_to_baidu(name, browser):
#     '''
#     :param name:    str
#     :param browser: webdriver.Chrome 实际应该是全局变量的
#     :return:        将要输入的 关键字 输入百度图片
#     '''
#     # 采用id进行xpath选择，id一般唯一
#     inputs = browser.find_element_by_xpath('//input[@id="kw"]')
#     inputs.clear()
#     inputs.send_keys(name)
#     time.sleep(1)
#     inputs.send_keys(Keys.ENTER)
#     time.sleep(1)
#
#     return
#
# def download_baidu_images(save_path, img_num, browser):
#     ''' 此函数应在
#     :param save_path: 下载路径 str
#     :param img_num:   下载图片数量 int
#     :param browser:   webdriver.Chrome
#     :return:
#     '''
#     if not os.path.exists(save_path):
#         os.makedirs(save_path)
#
#     img_link = browser.find_elements_by_xpath('//li/div[@class="imgbox"]/a/img[@class="main_img img-hover"]')
#     img_link[2].click()
#     # 切换窗口
#     windows = browser.window_handles
#     browser.switch_to.window(windows[-1])  # 切换到图像界面
#     time.sleep(random.random())
#
#     for i in range(img_num):
#         img_link_ = browser.find_element_by_xpath('//div/img[@class="currentImg"]')
#         src_link = img_link_.get_attribute('src')
#         print(src_link)
#         # 保存图片，使用urlib
#         img_name = uuid.uuid4()
#         urllib.request.urlretrieve(src_link, os.path.join(save_path, str(img_name) + '.jpg'))
#         # 关闭图像界面，并切换到外观界面
#         time.sleep(random.random())
#
#         # 点击下一张图片
#         browser.find_element_by_xpath('//span[@class="img-next"]').click()
#         time.sleep(random.random())
#
#     # 关闭当前窗口，并选择之前的窗口
#     browser.close()
#     browser.switch_to.window(windows[0])
#
#     return
#
# def main(names, save_root, img_num=[1000,], continue_num=0, is_open_chrome=False):
#     '''
#     :param names: list str
#     :param save_root: str
#     :param img_num: int list or int
#     :param continue_num: int 断点续爬开始索引
#     :param is_open_chrome: 爬虫是否打开浏览器爬取图像 bool default=False
#     :return:
#     '''
#     options = webdriver.ChromeOptions()
#     # 设置是否打开浏览器
#     if not is_open_chrome:
#         options.add_argument('--headless')  # 不打开浏览器
#     else:
#         prefs = {"profile.managed_default_content_settings.images": 2}
#         options.add_experimental_option("prefs", prefs)
#
#     browser = webdriver.Chrome(chrome_options=options)
#     browser.maximize_window()
#     browser.get(r'https://image.baidu.com/')
#     time.sleep(random.random())
#
#     assert type(names) == list, "names参数必须是字符串列表"
#     assert continue_num <= len(names), "中断续爬点需要小于爬虫任务数量"
#
#     if type(img_num) == int:
#         img_num = [img_num] * len(names)
#         print(img_num)
#     elif type(img_num) == list:
#         print(img_num)
#     else:
#         print("None, img_num 必须是int list or int")
#         return
#
#     for i in range(continue_num, len(names)):
#         name = names[i]
#         save_path = os.path.join(save_root, str(names.index(name)))  # 以索引作为文件夹名称
#         send_param_to_baidu(name, browser)
#         download_baidu_images(save_path=save_path, img_num=img_num[i], browser=browser)
#     # 全部关闭
#     browser.quit()
#     return
#
#
#
# if __name__=="__main__":
#
#     # main(names=['施工人员穿反光衣', '反光衣',],\
#     #      save_root=r'F:\Reflective_vests',\
#     #      img_num=500)
#
#     main(names=['森林积雪', '道路积雪', '建筑积雪', '山上积雪', '草原下雪', '小区积雪', '雪人堆', '蓝天白云下的建筑道路积雪'],\
#          save_root=r'F:\DataSets\snow\positive',\
#          img_num=[300, 300, 300, 100, 100, 100, 50, 50],\
#          continue_num=7)

import json
import os
import requests

from header import utl_header


path = 'E:/Crawling/baidu/戴头盔'
if not os.path.exists(path):
    os.mkdir(path)
header = {
    'User-Agent':utl_header.get_header()
}
keyword = input('请输入你想下载的内容：')
page = input('请输入你想爬取的页数：')
page = int(page) + 1
n = 0
pn = 1
# pn代表从第几张图片开始获取，百度图片下滑时默认一次性显示30张
for m in range(1, page):
    url = 'https://image.baidu.com/search/acjson?'
    param = {
        'tn': 'resultjson_com',
        'logid': '8019853459628308729',
        'ipn': 'rj',
        'ct': '201326592',
        'is': '',
        'fp': 'result',
        'queryWord': keyword,
        'cl': '2',
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'adpicid': '',
        'st': '',
        'z': '',
        'ic': '',
        'hd': '',
        'latest': '',
        'copyright': '',
        'word': keyword,
        's': '',
        'se': '',
        'tab': '',
        'width': '',
        'height': '',
        'face': '',
        'istype': '',
        'qc': '',
        'nc': '1',
        'fr': '',
        'expermode': '',
        'force': '',
        'cg': 'star',
        'pn': pn,
        'rn': '30',
        'gsm': '1e',
    }
    # 定义一个空列表，用于存放图片的URL
    image_url = list()
    # 将编码形式转换为utf-8
    response = requests.get(url=url, headers=header, params=param)
    response.encoding = 'utf-8'
    response = response.text

    # req = requests.get(url=url, headers=header, params=param)
    # html = re.findall('"thumbURL":"(.*?)"', req.text)
    # print(html)

    # response = response.replace("\\", "")
    # print(response)

    # 把字符串转换成json数据
    try:
        data_s = json.loads(response)
    except:
        print('error')
    a = data_s["data"]  # 提取data里的数据
    for i in range(len(a)-1):  # 去掉最后一个空数据
        data = a[i].get("thumbURL", "not exist")  # 防止报错key error
        image_url.append(data)

    for image_src in image_url:
        image_data = requests.get(url=image_src, headers=header).content
        image_name = 'anquantoukui_bd_4_{}'.format(n+1) + '.jpg'
        image_path = path + '/' + image_name
        with open(image_path, 'wb') as f:
            f.write(image_data)
            print(image_name, '下载完成！')
            f.close()
        n += 1
    pn += 29
