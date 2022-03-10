import requests
# 引用requests模块
url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'
# 请求歌曲评论的url参数前面的部分

for i in range(5):
    params = {
    'g_tk':'5381',
    'loginUin':'0', 
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'GB2312',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0',
    'cid':'205360772',
    'reqtype':'2',
    'biztype':'1',
    'topid':'102065756',
    'cmd':'6',
    'needmusiccrit':'0',
    'pagenum':str(i),
    'pagesize':'15',
    'lasthotcommentid':'song_102065756_3202544866_44059185',
    'domain':'qq.com',
    'ct':'24',
    'cv':'10101010'   
    }
    # 将参数封装为字典
    res_comments = requests.get(url,params=params)
    # 调用get方法，下载这个字典
    json_comments = res_comments.json()
    list_comments = json_comments['comment']['commentlist']
    for comment in list_comments:
        print(comment['rootcommentcontent'])
        print('-----------------------------------')


# 获取qq音乐中周杰伦的单曲
import requests
# 引用requests模块
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
for x in range(5):
    params = {
    'ct':'24',
    'qqmusic_ver': '1298',
    'new_json':'1',
    'remoteplace':'sizer.yqq.song_next',
    'searchid':'64405487069162918',
    't':'0',
    'aggr':'1',
    'cr':'1',
    'catZhida':'1',
    'lossless':'0',
    'flag_qc':'0',
    'p':str(x+1),
    'n':'20',
    'w':'周杰伦',
    'g_tk':'5381',
    'loginUin':'0',
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'utf-8',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0'    
    }
    # 将参数封装为字典
    res_music = requests.get(url,params=params)
    # 调用get方法，下载这个字典
    json_music = res_music.json()
    # 使用json()方法，将response对象，转为列表/字典
    list_music = json_music['data']['song']['list']
    # 一层一层地取字典，获取歌单列表
    for music in list_music:
    # list_music是一个列表，music是它里面的元素
        print(music['name'])
        # 以name为键，查找歌曲名
        print('所属专辑：'+music['album']['name'])
        # 查找专辑名
        print('播放时长：'+str(music['interval'])+'秒')
        # 查找播放时长
        print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html\n\n')
        # 查找播放链接