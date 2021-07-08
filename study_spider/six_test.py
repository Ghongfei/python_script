import requests

url = "https://www.baidu.com/"

proxies = {
    "https": "https://175.147.67.149:47242"
}

rep = requests.get(url, proxies=proxies)
rep.encoding = 'utf-8'

print(rep.text)