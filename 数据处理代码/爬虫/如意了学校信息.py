import xlsxwriter
from bs4 import BeautifulSoup
import urllib.request
import re
import random


header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.34 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.34'}
my_headers = [
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7',
    'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.34 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.34'
]

num1 = 1
workbook = xlsxwriter.Workbook('E:/hngz.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0, 0, '学校类型')
worksheet.write(0, 1, '名称')
worksheet.write(0, 2, '电话')
worksheet.write(0, 3, '邮编')
worksheet.write(0, 4, '地址')
for i in range(1, 6):
    pagesurl = 'https://www.ruyile.com/xuexiao/?a=20&t=5&p=' + str(i)
    req = urllib.request.Request(pagesurl, headers ={'User-Agent':random.choice(my_headers)})
    try:
        page = urllib.request.urlopen(req)
    except:
        print('error'+pagesurl)
        with open('E:/hngz.txt', 'a+') as f:
            f.write(pagesurl + '\n')
        continue
    data = page.read()
    data = data.decode('utf-8', 'ignore')
    soup1 = BeautifulSoup(data, features="lxml")
    pagess = soup1.select('.sk')


    for item in range(len(pagess)):

        school = pagess[item].a.text
        if school == '':
            school = pagess[item].img['alt']
        email = ''
        address = ''
        try:
            phone = re.search('电话：(.*?)地址', pagess[item].text).group(1)

        except:
            phone = ''
            print(pagesurl)
            continue
        try:
            address = re.search('地址：(.*)', pagess[item].text).group(1)
        except:
            address = ''
            print(pagesurl)
            continue
        worksheet.write(num1, 0, '普通高校')
        worksheet.write(num1, 1, str(school))
        worksheet.write(num1, 2, str(phone))
        worksheet.write(num1, 3, str(email))
        worksheet.write(num1, 4, str(address))
        num1 += 1
workbook.close()





