import os
import random
import json
import urllib.request

my_headers = [
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7',
    'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 '

]

json_path = r'E:\zhanku\cool\cool.json'

cou = 1
# for i in os.listdir(json_path):

f = open(json_path, encoding='utf-8')
res = f.read()

imgurl = json.loads(res)['data']['data']

for x in imgurl:
    imgurll = x['preview260_url']
    print(imgurll)
    opener = urllib.request.build_opener()
    opener.addheaders = random.choice(my_headers)
    req = urllib.request.urlopen(imgurll)
    data = req.read()

    path = r'E:\zhanku\斧头'
    if not os.path.exists(path):
        os.mkdir(path)
    outputpath = path + '\d_10_' + str(cou) + '.jpg'
    if os.path.exists(outputpath):
        print('image already exit')
        cou += 1
        continue
    f = open(outputpath, 'wb')
    f.write(data)
    print(outputpath + ' ' + 'ok')
    f.close
    cou += 1
