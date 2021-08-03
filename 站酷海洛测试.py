import requests
import json


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
}

data = {
    'keyword': "安全帽",
    'page': 2
}
url = 'https://api.hellorf.com/hellorf/image/search?version=staging'

req = requests.post(url, headers=headers, data=json.dumps(data))


if req.status_code == 200:
    print(req.text)