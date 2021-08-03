import requests, time
import json
from contextlib import closing

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
}


class get_photos(object):

    def __init__(self):
        self.photo_id = []
        self.download_url = 'https://unsplash.com/photos/xxx/download?force=trues'
        self.url = 'https://unsplash.com/napi/topics/nature/photos?page=1&per_page=20'

    def get_ids(self):
        req = requests.get(self.url, headers=headers)
        html = json.loads(req.text)
        for id in html:
            self.photo_id.append(id['id'])

        time.sleep(1)

    def download(self, photo_id, filename):
        url = self.download_url.replace('xxx', photo_id)
        with closing(requests.get(url=url, stream=True, headers=headers)) as r:
            with open('%d.jpg' % filename, 'ab+') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()


if __name__ == '__main__':
    gp = get_photos()
    print('获取图片连接中:')
    gp.get_ids()
    print('图片下载中:')
    for i in range(len(gp.photo_id)):
        print('  正在下载第%d张图片' % (i + 1))
        gp.download(gp.photo_id[i], (i + 1))
