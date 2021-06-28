import re
import os
import time

import requests
from header import utl_header


def downPic(dirs, keyword, imgId):
    headers_downPic = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'p9.pstatp.com',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '',
        'User-Agent': utl_header.get_header(),
    }
    url = 'https:////icweiliimg1.pstatp.com/weili/sm/{}.webp'.format(imgId)
    print("line20：   " + url)
    while True:
        try:
            res = requests.get(url, headers=headers_downPic)
            break
        except:
            time.sleep(30)

    savefile = os.path.join(dirs, keyword, imgId + ".jpg")
    if not os.path.exists(os.path.dirname(savefile)):
        os.makedirs(os.path.dirname(savefile))
    with open(savefile, 'wb') as f:
        f.write(res.content)
        f.close()
    print("下载成功! time ", time.ctime())


def visitContent(keyword, savePath):
    for page in range(2, 51):
        headers_visitContent = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'cookie': 'PHPSESSID=eb7kn10j6ed22srj8a9gg8upl3; webp_enabled=1; '
                      '_ga=GA1.2.1531772161.1540775429; _gid=GA1.2.1509491512.1540775429; '
                      'weilisessionid=c39a62f3e6996be04e27e693afd32488; wluuid=WLGEUST-0629E5A8-FD7F-BF5F-7C03-5621C88DAA08; '
                      'wlsource=tc_pc_home_search; webp_enabled=0; _ga=GA1.3.1531772161.1540775429; _gid=GA1.3.1509491512.1540775429;'
                      ' qimo_seosource_e7dfc0b0-b3b6-11e7-b58e-df773034efe4=%E7%AB%99%E5%86%85;'
                      ' qimo_seokeywords_e7dfc0b0-b3b6-11e7-b58e-df773034efe4=; '
                      'href=https%3A%2F%2Fstock.tuchong.com%2Fsearch%3Fsource%3Dtc_pc_home_'
                      'search%26term%3D%25E7%25BE%258E%25E5%25B0%2591%25E5%25A5%25B3; '
                      'accessId=e7dfc0b0-b3b6-11e7-b58e-df773034efe4; '
                      'bad_ide7dfc0b0-b3b6-11e7-b58e-df773034efe4=cb76ee61-db17-11e8-bb24-e322d5547169; '
                      'nice_ide7dfc0b0-b3b6-11e7-b58e-df773034efe4=cb76ee62-db17-11e8-bb24-e322d5547169; '
                      'wltoken=2dac12af5bfe5c47; wluserid=596443; wlnickname=%E4%B8%AA%E4%BA%BA%E4%B8%AD%E5%BF%83; pageViewNum=16',
            'pragma': 'no-cache',
            'upgrade-insecure-requests': '',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
        }
        # url = "https://stock.tuchong.com/search?term={keyword}&use=0&type=2&layout=&sort=0&category=0&page={page}&size=200&search_from=head&exact=0&platform=weili&tp=&abtest=&royalty_free=0&option=&has_person=2&face_num=1&gender=0&age=&racial=".format(keyword=keyword,page=page,)
        url = "https://stock.tuchong.com/search?id=&term={keyword}&no_overwrite=&use=0&type=&layout=&sort=0&category=0&size=100&exact=0&platform=weili&tp=&abtest=&royalty_free=0&image_source=&option=&has_person=0&face_num=&gender=0&age=&racial=&samemodel=0".format(
            keyword=keyword, page=page, )
        print("48：  " + url)

        while True:
            try:
                res = requests.get(url, headers=headers_visitContent)
                break
            except:
                time.sleep(30)
        imgIds = re.findall(r'{"imageId":"(.*?)"', res.text)
        for imgId in imgIds:
            downPic(savePath, keyword, imgId)


if __name__ == '__main__':

    keywords = ["抽烟", ]
    savePath = r"E:\tuchong"

    if not os.path.exists(savePath):
        os.makedirs(savePath)
    for keyword in keywords:
        visitContent(keyword, savePath)