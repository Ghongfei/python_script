import urllib.request
import random
from bs4 import BeautifulSoup

# soup = BeautifulSoup(open('D:/pig/html/a4.html',encoding='utf-8'),features='lxml')
cou = 895
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

list = []
#for i in range(30, 31):
soup = BeautifulSoup(open('E:/安全帽/a1.html', encoding='utf-8'), features='lxml')
for imgspan in soup.select('.imgpage'):
    for imglist in imgspan.select('.imgitem'):
        url = imglist['data-objurl']
        if url[-3:] != 'png':
            list.append(url)
print(len(list))
for index, i in enumerate(list):
    if index >= 100:
        # print(index)
        req4 = urllib.request.Request(i, headers={'User-Agent': random.choice(my_headers)})
        try:
            finalpage = urllib.request.urlopen(req4)
            itdata = finalpage.read()
            imggname = 'E:/安全帽/负样本/nonsafety_hat' + str(cou) + '.jpg'
        except:
            continue

        # if os.path.exists(imggname) == True:
        #     cou += 1
        #     print(imggname + 'allready in the fire')
        #     continue
        # else:
        f = open(imggname, "wb")
        f.write(itdata)
        f.close()
        print(imggname + 'ok')
        cou += 1


