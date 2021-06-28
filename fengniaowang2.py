#conding=utf-8

# import requests
# import json
#
# def download(img_url, img_name):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101'
#     }
#     req = requests.get(img_url, headers=headers)
#     path = r'E:\Crawling\veer\工人高空作业'
#     file_name = path + '\\' + img_name+img_url[-13:]#图片名为描述+图片的编号
#     f = open(file_name, 'wb')
#     f.write(req.content)#以字节流的形式读入文件
#     f.close
#
#
# def get_list(name, type, page):
#
#     for i in range(int(page)):
#         page_num = i
#
#         url = 'https://www.veer.com/ajax/search'  # URL
#         header = {
#             'content-type': 'application/json',
#             'Host': 'www.veer.com',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
#         }
#         payloadData = {
#             'graphicalStyle': type, #类型：1.照片 2.插画 3.矢量图 Nan为全部
#             'page': page_num,  #分页数量
#             'page_type': 6, #分页的格式，这个不重要
#             'perpage': 10000, #一页多少图片
#             'phrase': name #搜索的关键字
#         }# 分页数量为1，一页10000，是为了尽量只从一个页面上的到所有的list
#         html = requests.post(url, data=json.dumps(payloadData), proxies={"http" : "http:// 115.225.74.53: 8118"}, headers=header).text #payloadData要求用josn来进行解析，代理ip自己去爬取，
#         list = json.loads(html)#获取json解析的list，不然全是乱码
#         data = list['data'] #封装成字典格式
#         print("总共搜索到图片：",data['totalCount'], "张图片")
#         id = data['list']
#         for sid in id:
#             print(sid['oss400'], sid['cnTitle'])#用的是400的，为了veer的利益，不采用1600尺寸的图片
#             if sid['cnTitle']==None:#防止图片描述为空
#                 sid['cnTitle'] = "none"
#             download('https:'+sid['oss400'], sid['cnTitle'])#进行下载
#
#
#
# if __name__ == '__main__':
#     print("输入搜索图片名称：")
#     name = input()
#     print("选择图片类型1.照片 2.插画 3.矢量图 4.所有")
#     type  = input()
#     print("输入页数：")
#     page = input()
#     if type>'3':
#         type=""
#     get_list(name, type, page)


import requests
import json
import os


photo_dir = r'E:\Crawling\veer'

def download(img_url, img_name):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101'
    }

    req = requests.get(img_url, headers=headers)

    file_name = word_dir + '\\' + img_name + img_url[-13:]
    f = open(file_name, 'wb')
    f.write(req.content)
    f.close


def get_picture(name, i):
    url = 'https://www.veer.com/ajax/search'
    print("i：" + str(i))

    header = {
        'content-type': 'application/json',
        'Cookie': '_ga=GA1.2.1116465633.1600825938; _gid=GA1.2.1173248234.1622107577; queryKey=HNA1L65DL59; Hm_lvt_f2de34005a64c75f44715498bcb136f9=1620786093,'
                  '1621933693,1622193082; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22916430%22%2C%22first_id%22%3A%22174b8a94bc3516-0980e317'
                  'd6f47d-3a65420e-2073600-174b8a94bc4a7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%'
                  '2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3'
                  'A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.veer.com%2Fsearch-image%2Fdaitoukuiqiche%2F%3Fpage%3D3%22%2C%22%24latest_utm_sour'
                  'ce%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22cpc%22%2C%22%24latest_utm_campaign%22%3A%22%E9%80%9A%E7%94%A8%E8%AF%8D-%E5%9B%BE%E7%89%87'
                  '%22%2C%22%24latest_utm_content%22%3A%22%E9%80%9A%E7%94%A8%E8%AF%8D-%E5%9B%BE%E7%89%87-%E5%A4%96%E5%9B%BD%22%2C%22%24latest_utm_term%22%3A%22%E5%'
                  '9B%BD%E5%A4%96%E5%9B%BE%E7%89%87%E7%B4%A0%E6%9D%90%22%7D%2C%22%24device_id%22%3A%22174b8a94bc3516-0980e317d6f47d-3a65420e-2073600-174b8a94bc4a7%'
                  '22%7D; acw_tc=2760828e16221944355042568ebfdbc22fee541f7153ae8dc17494ecd504be; acw_sc__v3=60b0bc3674e77ac16ae1c6f1380d5cc1cf041efd; _gat=1; _gat_g'
                  'tag_UA_103598720_1=1; views=8; Hm_lpvt_f2de34005a64c75f44715498bcb136f9=1622195383; acw_sc__v2=60b0bcb6bf54ce46392cc80c3e90f8b1613c8489; _fp_=eyJp'
                  'cCI6IjU5LjQxLjE2My4xNzgiLCJmcCI6ImI1MjRjNTYxNWY2MjFlM2FjYTBjNzdjM2MyOGVhZjRlIiwiaHMiOiIkMmEkMDgkVUk4OW92RUxkTGFjQ05SdDBmMGkvLmQucEVKcnd0Q1RrR2hoT0'
                  'dyQ3ZyNHk1Sm9YQmR3dS4ifQ%3D%3D; ssxmod_itna=Wu0=iIqjxGraGHD8D2DEfePmuDQTrhRDDtizQFWDlr=DxA5D8D6DQeGTinbmQi57C7DqbPFrnup=xkamrdbbGbE0naz0/MPGLDmKDy'
                  'lCDYeDxhq0rD74irDDxD3Db4QDSDWKD9+qi3DElKDYxDrXpKDRxi7DDvQzx07DQykeSP+BxE1ziYPWlKD9ooDs=0AQlKwm83qV6b8DlKjDCIzBZF1i4GdDo235YxeVCGoO=p5bYbae1bxQimqz'
                  'n2PUi2x+nrxHYQyWDDWWm4eXihDD; ssxmod_itna2=Wu0=iIqjxGraGHD8D2DEfePmuDQTrhRDDtizQWD6E4tYx05Pweo03mQkb98q30DnRxkQjrh+i+KHDwotN4EiW224keRuYKpP6x3Lyqo5'
                  'ScTnG8NzYf2RWKYMFiP1ftuqiW93wpeXGAG5xhoN/Udf8tlABmGYSj4I4DmA2GEeXAYfqWqt7mD0MD+T/KlD7f36w9mN+lQckISW7N3KbqmE7mYaHwxTCN+hNvuajeQTbmg2Ofc9WvfvmN0A69'
                  'm5Hwf3jp2YehERwb+AxPUQwYEDv8ZYGb1ikxs8hlAbet8wlmbhg96vB4nqDRq24Yx2zqOd27YoBi8LCYoaKbT4rep3huMOqSsb0=m8+xSOkLwr8m83KpmQNfH4gKkhQMg=3mh2WYaE8SdT3jTm'
                  'oaahemxi231praslr2bvlgKjoQxOEvR=HL=LwwsLWjT1XOWOSWNRWsSf7OoL4jyCje4ilDdfED4kjnuf7d1v6LZ7=fua2gjqBWfhTA+Lsw8ZAL1bN131K8dDhw9iWPbkcfiqIdm82R0IZYo=zd'
                  'VAj5r89=xfDDwZvI0jEjN5V4CBYGGmcjSrA9BmSWBuOm087k3eQQGq1wwn2jVCw1WPi=G=DGcDG7QiDD==',
        'Host': 'www.veer.com',
        'Origin': 'https://www.veer.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
    }

    payloadData = {
        'graphicalStyle': '',
        'phrase': name,
        'page': i,
        'perpage': 1000,
        'page_type': 6,
        'favorid': ''
    }

    html = requests.post(url, data=json.dumps(payloadData), headers=header)

    try:
        list = json.loads(html.text)
    except:
        print('error')

    data = list['data']
    print("总共搜索到图片：", data['totalCount'], "张图片")
    id = data['list']
    j = 0
    for sid in id:
        try:
            if sid['cnTitle'] == None:
                sid['cnTitle'] = "none"
            url_400 = 'https:' + sid['oss400']
            download(url_400, sid['cnTitle'])
            j = j + 1
        except Exception as e:
            print('Error: ', sid)

    return j


def get_num_list(name, page_num):
    picture_all = 0
    name = name
    for i in range(100, page_num + 1):

        picture_num = get_picture(name, i)
        print("page_num：", i, "   picture_num: ", picture_num)
        picture_all = picture_all + picture_num
        print("get_picture_all:", picture_all)

    print('Done!')


if __name__ == '__main__':

    name = input("输入搜索图片名称：")
    word_dir = os.path.join(photo_dir, name)

    if not os.path.exists(word_dir):
        os.mkdir(word_dir)

    page_num = input("请输入爬取的页数：")

    while (page_num == ""):
        print("爬取的页数不能为空")
        page_num = input("请输入爬取的页数(每页200张图片)：")
    else:
        page_num = int(page_num)
        get_num_list(name, page_num)