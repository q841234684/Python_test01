import json

import requests


def get01():
    param = dict([('q', 'python'), ('cat', '1001')])
    r = requests.get('https://www.douban.com/', params=param)
    print(r.url, '\n', r.content.decode('utf-8'))
    print('------------------------------')
    print(r.cookies)
    print(r.status_code)
    print(r.encoding)


def getJson():
    r = requests.get(
        "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json")
    # requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取：
    jsons = r.json()
    print(type(jsons))
    created = jsons['query']['created']
    print(created)
    # print(r.content)


def add_header():
    r = requests.get('https://www.douban.com/',
                     headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
    print(r.content.decode("utf-8"))

# requests默认使用application/x-www-form-urlencoded对POST数据编码。
def post01():
    username = input('Email:')
    passwd = input('passwd:')
    data = dict([('username', username),
                 ('password', passwd),
                 ('entry', 'mweibo'),
                 ('client_id', ''),
                 ('savestate', '1'),
                 ('ec', ''),
                 ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')])
    header = dict([('Origin', 'https://passport.weibo.cn'),
                   ('User-Agent',
                    'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'),
                   ('Referer',
                    'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')])
    r = requests.post('https://passport.weibo.cn/sso/login', data=data, headers=header)
    print(r.status_code)


def login():
    data = {'username': 'admin', 'password': '123'}
    s=requests.session()
    r = s.post('http://localhost:8080/login', data=data)
    print(r.content.decode('utf-8'))
    return s

# 如果要传递JSON数据，可以直接传入json参数：
def tran_json():
    params = {'key': 'value'}
    # r = requests.post(url, json=params) # 内部自动序列化为JSON

def upload_file():
    s=login()
    uploadfile={'image':open('../resource/cat.jpg','rb')}
    post = s.post('http://localhost:8080/uploadImage', files=uploadfile)
    print(post.content.decode('utf-8'))
    print(post.status_code)

if __name__ == '__main__':
    # get01()
    # getJson()
    # add_header()
    # post01()
    # login()
    upload_file()
