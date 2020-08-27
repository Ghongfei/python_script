import requests
import re
import json
import base64

page_url = 'https://www.ixigua.com/i6717973108818444814/'

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
headers = {
    "User-Agent": user_agent
}
page_content = requests.get(page_url, headers=headers).content.decode(encoding='utf-8');
# print(page_content)

config_info = re.findall(r'window\.__pageState=.*\}</script>', page_content)[0]
config_info = json.loads(config_info.split('window.__pageState=')[1].replace('</script>', ''))['video']

title = config_info['title']

v_sdk = 'https://vas.snssdk.com/video/openapi/v1/'
params = {
    'action': 'GetPlayInfo',
    'video_id': config_info['vid'],
    'nobase64': 'false',
    'ptoken': config_info['businessToken'],
    'vfrom': 'xgplayer'
}
v_header = {
    'Authorization': config_info['authToken'],
    "User-Agent": user_agent
}
video_info = json.loads(requests.get(v_sdk, params=params, headers=v_header).content.decode())
if video_info['code'] == 0:
    h_video = video_info['data']['video_list']['video_' + str(video_info['total'])]
    v_type = h_video['vtype']
    video_url = str(base64.urlsafe_b64decode(h_video['main_url']), encoding='utf-8')
    print(title)
    print(video_url)
    with open('./%s.%s' % (title, v_type),'wb') as f:
        f.write(requests.get(video_url).content)
    print('下载成功！')
else:
    print('请求失败!')


