# coding:utf-8
import xlrd
import xlwt
import requests
import urllib
import math
import re
import os
from xlutils.copy import copy
pattern_x = re.compile(r'"x":(".+?")')
pattern_y = re.compile(r'"y":(".+?")')
 
 
def mercator2wgs84(mercator):
    # key1=mercator.keys()[0]
    # key2=mercator.keys()[1]
    point_x = mercator[0]
    point_y = mercator[1]
    x = point_x / 20037508.3427892 * 180
    y = point_y / 20037508.3427892 * 180
    y = 180 / math.pi * (2 * math.atan(math.exp(y * math.pi / 180)) - math.pi / 2)
    return (x, y)
 
 
def get_mercator(addr):
    quote_addr = urllib.parse.quote(addr.encode('utf8'))
    
    s = urllib.parse.quote(u'广东省'.encode('utf8'))
    api_addr = "http://api.map.baidu.com/?qt=gc&wd=%s&cn=%s&ie=utf-8&oue=1&fromproduct=jsapi&res=api&callback=BMap._rd._cbk62300" % (
        quote_addr
        , s)
    req = requests.get(api_addr)
    content = req.text
    x = re.findall(pattern_x, content)
    y = re.findall(pattern_y, content)
    if x:
        x = x[0]
        y = y[0]
        x = x[1:-1]
        y = y[1:-1]
        x = float(x)
        y = float(y)
        location = (x, y)
    else:
        location = ()
    return location
 
 
def run():
    for file in os.listdir('D:/学校/学校/'):
        print(file)
        data = xlrd.open_workbook('D:/学校/学校/' + file)
        
        
        rtable = data.sheets()[0]
        nrows = rtable.nrows
        values = rtable.col_values(1)[1:]

        
        sheets = data.sheet_names()  # 获取工作簿中的所有表格
        worksheet = data.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
        new_workbook = copy(data)
        new_worksheet = new_workbook.get_sheet(0)
        
        new_worksheet.write(0, 6, '经纬度')
        #workbook = xlwt.Workbook()
        #wtable = workbook.add_sheet('data', cell_overwrite_ok=True)
        row = 1
        for value in values:
            mercator = get_mercator(value)
            if mercator:
                wgs = mercator2wgs84(mercator)
            else:
                wgs = ('NotFound', 'NotFound')
            print("%s,%s,%s" % (value, wgs[0], wgs[1]))
            print(type(wgs[0]))
            new_worksheet.write(row, 6, str(wgs[0]) + ','+ str(wgs[1]))
            row = row + 1
     
        new_workbook.save('D:/学校/学校/' + file)
 
 
if __name__ == '__main__':
    run()
