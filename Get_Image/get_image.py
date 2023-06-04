import requests

class getImage():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'Referer': 'www.pixiv.net',
            'Content-Type': 'application/json'
        }
    
    def get_image(self, r18=0, num=1, uid=[''], tag=[''], excludeAI='false'):
        #使用POST请求获取网页返回的json数据
        url = 'https://api.lolicon.app/setu/v2'
        payload = {'r18': r18, 'num': num, 'uid': uid, 'tag': tag, 'excludeAI': excludeAI}
        r = requests.post(url, json=payload, headers=self.headers).json()
        #print(r)
        
        #下载图片到本地
        for i in range(1, num + 1):
            with open('./pics/{i}.{ext}'.format(i=i, ext=r['data'][i - 1]['ext']), mode='wb') as f:
                res = requests.get(r['data'][i - 1]['urls']['original'], headers=self.headers)
                f.write(res.content)
