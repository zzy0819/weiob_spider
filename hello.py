import requests
import time
import re
import datetime


header ={ 'cookie':'SINAGLOBAL=5784854338978.618.1645952940940; UOR=,,www.baidu.com; XSRF-TOKEN=J-yb21YEqmGuYSc7ZgrvRUGA; _s_tentry=weibo.com; appkey=; Apache=6127196369241.557.1660215319304; ULV=1660215319307:1:1:1:6127196369241.557.1660215319304:; SSOLoginState=1660215363; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWQMAloU.ml-c9CXFox2M9J5JpX5KMhUgL.FoMfeo.XSo5NehB2dJLoIEqLxK-LBKBLBoBLxKMLB.zL1K.LxKBLB.BLBKW.qCH8Sb-RxC-R1Btt; webim_unReadCount={"time":1661523736560,"dm_pub_total":66,"chat_group_client":0,"chat_group_notice":0,"allcountNum":115,"msgbox":0}; WBPSESS=Cf4W5uo8ft94DkKLhJc1YROGvx56CHXkTJx1QFtNvSgUl2QicvkghN88tyZjnpUFBhlKTc75zhI-wE5g8iMgUh42LU1z6nDmTM5WLpZZc1xPVR8p_amZuUF8ikhkOeiA-qD-Gp9Ha1Bx3UgBQJ2V_w==; SCF=Ah3hm3TdiGiew31A1yKvPrZwaA2dLLO57MNvRGSmAmf1RrrBBq4n723edNPIvVabAwoN40K9yAgfsMXA_q1YozE.; SUB=_2A25ODm8qDeRhGeFL6VsV9i7LyziIHXVtesfirDV8PUNbmtAKLW_NkW9NQi1hexrd704RlkZzf3su52en7MEoZvRz; ALF=1693143802',
          'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}


user_id = 7529460704
weibo_requests_url = 'https://weibo.com/ajax/statuses/mymblog?uid=3176010690&page=1&feature=0'
count_weibo_url = 'https://weibo.com/ajax/profile/info?uid=7529460704'


# 获取最近一次发博时间
def get_the_new():
    response = requests.get(weibo_requests_url, headers=header)
    if response.status_code == 200:
        item = response.json()
        # print(item['data']['list'][0]['created_at'])
        # 使用正则表达式提取时分
        time_01 = re.search('\d\d:\d\d', item['data']['list'][1]['created_at'])
        # print(time_01.group(0))
        return time_01.group(0)
    else:
        print('error')
        print(response)


def check_new():
    weibo_time = get_the_new()
    i = datetime.datetime.now()
    # print(str(i.hour) + ":" + str(i.minute))
    s_time = str(i.hour) + ":" + str(i.minute)
    if s_time == weibo_time:
        print("用户刚刚发博了"+s_time)
    else:
        print("用户暂无发博,上次发博时间"+weibo_time)


while(1):
    check_new()
    time.sleep(5)



