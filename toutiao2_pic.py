import requests, os
from urllib.parse import urlencode
# 当前路径
# path_a = os.path.abspath('.')
path_a = r"E:\toutiao2"
kw = ''

while True:
    kw = input('请输入关键词(1为退出)：')
    if kw == '1':
        print('退出，你下载的图片在' + path_a)
        break
    for x in range(0, 1000, 20):
        url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=' + str(x) +'&format=json&keyword=' + kw + '&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab'
        response = requests.get(url)
        data = response.json()['data']
        if not data:
            print('下载完成，请换关键词！')
            break
        n = 1 # 记录文章数
        for atlas in data:
            # 创建目录
            if not os.path.exists(path_a):
                os.mkdir(path_a)
            k = 1 # 记录下载的图片数
            # 转进图片目录
            os.chdir(path_a)
            for image in atlas['image_list']: # 这个链接获取的图片是小张的
                # image_url = image['url'].replace('list', 'large') # 改成大张的
                atlas = requests.get(image['url']).content
                with open(str(k) + '.jpg', 'wb') as f:
                    f.write(atlas)
                print('下载完第%d个文章的%d图！'%(x+n, k))
                k += 1
            n += 1
            # 转出图片目录
            os.chdir(path_a)