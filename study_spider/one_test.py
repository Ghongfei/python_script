from urllib.request import urlopen


url = 'http://www.baidu.com'
resp = urlopen(url)
with open('./baidu.html', mode="w", encoding="utf-8") as f:
    f.write(resp.read().decode('utf-8'))

