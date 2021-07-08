import xlsxwriter
from bs4 import BeautifulSoup
import urllib.request
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

num1 =0
workbook = xlsxwriter.Workbook('E:/aa1.xlsx')
worksheet = workbook.add_worksheet()

f = open('E:/hnzhong.txt')

for line in f:

    link = line.strip('\n')
    req1 = urllib.request.Request(link, headers={'User-Agent': random.choice(my_headers)})
    try:
        page1 = urllib.request.urlopen(req1)
    except:
        print(link)
        continue
    data1 = page1.read()
    data1 = data1.decode('utf-8', 'ignore')
    soup11 = BeautifulSoup(data1, features="lxml")
    school = soup11.select('.header')[0]
    school = school.strong.text

    xxsx = soup11.select('.xxsx')[0].select('div')
    phone = xxsx[4].text.split('：')[1]
    address = xxsx[7].text.split('：')[1]
    email = xxsx[8].text.split('：')[1]

    worksheet.write(num1, 0, '中学')
    worksheet.write(num1, 1, str(school))
    worksheet.write(num1, 2, str(phone))
    worksheet.write(num1, 3, str(email))
    worksheet.write(num1, 4, str(address))
    num1 += 1
workbook.close()



