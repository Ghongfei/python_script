import requests
import re
import os

imagIds = re.compile('"imageId":"(.*?)"')

headers = {
    "User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.59",
    "Accept-Encoding":""
}

def get_page():
    for i in range(1,100):
        url = "https://premium.tuchong.com/search?term=%E5%B7%A5%E4%BA%BA%E9%AB%98%E7%A9%BA%E4%BD%9C%E4%B8%9A&no_overwrite=&use=0&type=&layout=&sort=0&category=0&page={}&size=100&search_from=&exact=0&platform=creativevip&tp=&abtest=&royalty_free=0&image_source=&photographerId=0&photographerName=&option=&tiff_size_from=0&tiff_size_to=0&color=&has_person=0&face_num=&gender=0&age=&racial=&samemodel=0&price=0&image_format=&is_need_overwrite=true".format(i)
        html = requests.get(url,headers=headers)
        results = imagIds.finditer(html.text)
        for r in results:
            imgurl = 'https://icweiliimg1.pstatp.com/weili/smh/{}.jpg'.format(r.groups()[0])
            download_img(imgurl,r.groups()[0])

def download_img(url,name):
    path = r"E:\Crawling\tuchong"
    if not os.path.exists(path):
        os.mkdir(path)

    print('正在下载图片，ID：'+name)
    try:
        with open(path + "\\belt_tuc_0002_{}.jpg".format(name),'wb') as f:
            print(url)
            f.write(requests.get(url,headers=headers).content)
            f.close()
    except:
        print("error")

if __name__ == '__main__':
    get_page()