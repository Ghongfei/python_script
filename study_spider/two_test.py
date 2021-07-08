import requests
import re
import csv


headers = {
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'
}

url = 'https://movie.douban.com/chart'
req = requests.get(url, headers=headers)
content = req.text

obj = re.compile(r'<td valign="top">.*?<span style="font-size:13px;">(?P<name>.*?)</span>.*?'
                 r'<p class="pl">(?P<pl>.*?)</p>',re.S)

names = obj.finditer(content)
f = open("dianyin.csv", mode='w', encoding='utf-8')

csvwriter = csv.writer(f)

for name in names:
    dic = name.groupdict()
    csvwriter.writerow(dic.values())

f.close()

print('over')