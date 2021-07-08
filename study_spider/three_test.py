import requests
import re

headers = {
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"
}

url = 'https://www.dy2018.com/'

resp = requests.get(url, headers=headers)
resp.encoding = 'gb2312'


obj1 = re.compile(r'2021必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)
obj2 = re.compile(r"<a href='(?P<url>.*?)'",re.S)

url_list = []

uls = obj1.finditer(resp.text)
for ul in uls:
    ul = ul.group("ul")

    lis = obj2.finditer(ul)
    for li in lis:
        url_href = url + li.group("url").strip("/")
        url_list.append(url_href)


for url_c in url_list:
    print(url_c)