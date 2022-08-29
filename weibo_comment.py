from urllib.parse import urlencode
import requests
from pyquery import pyquery as pq
import re
base_url = 'https://weibo.com/ajax/statuses/buildComments?'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'cookie':'SINAGLOBAL=5784854338978.618.1645952940940; UOR=,,www.baidu.com; XSRF-TOKEN=cGyz1yhaVdGDCHJK3cREOpQx; SSOLoginState=1659012680; _s_tentry=weibo.com; Apache=4192147442809.8325.1659012691335; ULV=1659012691443:28:1:1:4192147442809.8325.1659012691335:1655629367070; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWQMAloU.ml-c9CXFox2M9J5JpX5KMhUgL.FoMfeo.XSo5NehB2dJLoIEqLxK-LBKBLBoBLxKMLB.zL1K.LxKBLB.BLBKW.qCH8Sb-RxC-R1Btt; ALF=1691413288; SCF=Ah3hm3TdiGiew31A1yKvPrZwaA2dLLO57MNvRGSmAmf1ON8r_XjNfjbZ3qHp34OEq7s3469xb4-8RrTueu5qjig.; SUB=_2A25P68f5DeRhGeFL6VsV9i7LyziIHXVsgL4xrDV8PUNbmtAKLWzRkW9NQi1hexeQGR2RZ2_5uORsJ6YCzEYS2erA; WBPSESS=Cf4W5uo8ft94DkKLhJc1YROGvx56CHXkTJx1QFtNvSgUl2QicvkghN88tyZjnpUFBhlKTc75zhI-wE5g8iMgUoJJ_2BGJdgG2z0No16XfTXxElKlhgnyYl88bfDNB9JFUX-mM7mhxXaf-NkIUxWXow=='
    }


the_max_id = 0


def get_page(the_max_id):
    params = {
            #排列方式  0为
            'flow': 0,
            # 是否为为重新加载
            'is_reload': 0,
            'id': 4802807482027088,
            'is_show_bulletin': 2,
            'is_mix': 1,
            'fetch_level':1,
            'max_id': 0,
            'count': 250,
            'uid': 3176010690
    }
    url = base_url + urlencode(params)
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("error")


def parse_page(json):
    file_name = '1.jpg'
    i = 1
    items = json.get('data')
    for item in items:
        content = item['text']
        url = re.search('href="(.*?)">', content)
        if url != None :
            file_name = './image_1/'+ str(i) + '.jpg'
            i = i + 1
            print(url.group(1))
            r = requests.get(url.group(1), headers=headers)
            with open(file_name, 'wb') as f:
                f.write(r.content)


def run():

    json = get_page(the_max_id)
    parse_page(json)


run()

