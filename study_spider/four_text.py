import requests
from bs4 import BeautifulSoup

url = "http://www.baidu.com/"

headers = {
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"
}

res = requests.get(url,headers=headers)

pas =  BeautifulSoup(res.text, "html.parser")