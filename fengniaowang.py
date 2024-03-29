import aiohttp
import asyncio
import os
import json
import urllib

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
           "X-Requested-With": "XMLHttpRequest",
           "Accept": "*/*"}

sema = asyncio.Semaphore(3)


async def get_source(url):
    print("正在操作:{}".format(url))
    conn = aiohttp.TCPConnector(verify_ssl=False)  # 防止ssl报错,其中一种写法
    async with aiohttp.ClientSession(connector=conn) as session:  # 创建session
        async with session.get(url, headers=headers, timeout=10) as response:  # 获得网络请求
            if response.status == 200:  # 判断返回的请求码
                source = await response.text()  # 使用await关键字获取返回结果
                try:
                    data = json.loads(source)
                except:
                    print('error')
                # photos = data["photos"]["photo"]
                photos = data["data"]["list"]
                for p in photos:
                    # img = p["src"].split('?')[0]
                    img = p["oss400"]
                    try:
                        async with session.get(img, headers=headers) as img_res:
                            imgcode = await img_res.read()
                            path = r'E:\Crawling\fengniao'
                            if not os.path.exists(path):
                                os.mkdir(path)
                            with open(path + "\{}".format(img.split('/')[-1]), 'wb') as f:
                                f.write(imgcode)
                                f.close()
                    except Exception as e:
                        print(e)
            else:
                print("网页访问失败")


# 为避免爬虫一次性请求次数太多，控制一下
async def x_get_source(url):
    with(await sema):
        await get_source(url)


if __name__=="__main__":

    # url_format = "https://tu.fengniao.com/ajax/ajaxTuPicList.php?page={}&tagsId=15&action=getPicLists"

    word = '戴头盔骑车'

    word = urllib.request.quote(word)
    url_format = 'https://www.veer.com/ajax/search?phrase={word}&page={page}'
    full_urllist = [url_format.format(word=word,page=i) for i in range(1, 200)]

    event_loop = asyncio.get_event_loop()  # 创建事件循环
    tasks = [x_get_source(url) for url in full_urllist]
    results = event_loop.run_until_complete(asyncio.wait(tasks))  # 等待任务结束