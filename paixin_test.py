import requests
import json


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'Referer': 'https://www.paixin.com/',
    'Content-Type': 'application/json;charset=UTF-8'
}


data = {
    'searchQuery': '头盔',
    'type': '6'
}
url = 'https://api2.paixin.com/medias/1/search?page=0&size=50&mix=true'

req = requests.post(url, headers=headers, data=json.dumps(data), timeout=3)
if req.status_code == 200:
    print(req.text)

