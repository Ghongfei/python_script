# from urllib.request import HTTPHandler, build_opener
# from collections import namedtuple
#
#
# Respone = namedtuple('Respone',
#                      field_names = ['headers','code','text','body'])
#
#
# def get(url):
#     opener = build_opener(HTTPHandler())
#     resp = opener.open(url)
#
#
#     headers = dict(resp.getheaders())
#     try:
#         encoding = headers['Content-Type'].split('=')[-1]
#     except:
#         encoding = 'utf-8'
#     code = resp.code
#     body = resp.read()
#     text = body.decode(encoding)
#
#     return Respone(headers = headers,
#                    code = code,
#                    body = body,
#                    text = text)
#
#
# if __name__ == '__main__':
#     resp: Respone =  get('https://jd.com')
#     print(resp.code)
#     print(resp.headers)



import itertools

i = 0

for item in itertools.count(start=0, step=60):

    i += 1

    if i > 10: break

    print(item)