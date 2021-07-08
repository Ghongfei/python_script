# -*- coding: utf-8 -*-
__author__ = 'thesby'
'''
    说明：本程序功能是通过读取一个excel表格中的位置信息，然后通过百度地图API返回对应的经纬度
    注意：1、运行程序前需要在程序所在文件夹中放入一个名为  book1.xls  的文件，并且在第一列放入地址信息。
            程序会把处理结果放入 data.xls 文件中。
         2、程序在 python2 版本上运行
'''
import xlrd
import xlwt
import urllib
import re
import requests
import os

def get_mercator(addr):
    '''addr: 输入的位置
    location：函数返回的一个元组，包含经度和纬度
    '''

    quote_addr = urllib.parse.quote(addr.encode('utf8'))
    # print addr
    # print quote_addr
    city = urllib.parse.quote(u'成都市'.encode('utf8'))
    province = urllib.parse.quote(u'四川省'.encode('utf8'))
    if quote_addr.startswith(city) or quote_addr.endswith(province):
        pass
    else:
        quote_addr = city + quote_addr
    s = urllib.parse.quote(u'北京'.encode('utf8'))
    api_add = 'http://api.map.baidu.com/geocoder/v2/?ak=%s&callback=renderOption&output=json&address=%s&city=%s' % ('xoYOXe7HD6yhqlXsHBtW88oK7l7t5TUC', quote_addr, s)
    req = requests.get(api_add)
    content = req.content
    longitude_pattern = re.compile(r'"lng":[0-9]{1,3}.[0-9]{0,12}')
    latitude_pattern = re.compile(r'"lat":[0-9]{1,3}.[0-9]{0,12}')
    lng = re.findall(longitude_pattern, content)
    lat = re.findall(latitude_pattern, content)
    # print lng,'  ', lat
    if lng:
        lng = float(lng[0][6:])
        lat = float(lat[0][6:])
        location = (lng, lat)
    else:
        location = ()
    return location


def run():
    for file in os.listdir('D:/学校/'):
        data = xlrd.open_workbook(u'D:/学校/' + file)
        rtable = data.sheets()[0]  # 第 0 张表格
        nrows = rtable.nrows  # 获取行数
        values = rtable.col_values(1)  # 获取第 1 行的所有值
        workbook = xlwt.Workbook()
        wtable = workbook.add_sheet('data', cell_overwrite_ok=True)  # 如果存在数据，则会被覆盖
        row = 0
        for value in values:
            mercator = get_mercator(value)
            if mercator:
                wgs = mercator
            else:
                print
                "Fatal Error: 没有得到百度地图API的正确数据返回"
                return -1
            if row == 0:
                wtable.write(row, 0, u'Address'.encode('utf8'))
                wtable.write(row, 1, u'longitude')
                wtable.write(row, 2, u'latitude')
                row += 1
                wtable.write(row, 0, value)
                wtable.write(row, 1, wgs[0])
                wtable.write(row, 2, wgs[1])
            else:
                wtable.write(row, 0, value)
                wtable.write(row, 1, wgs[0])
                wtable.write(row, 2, wgs[1])
            row += 1
        workbook.save('data.xls')


if __name__ == '__main__':
    run()


# xoYOXe7HD6yhqlXsHBtW88oK7l7t5TUC