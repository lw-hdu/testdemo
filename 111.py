'''
Descripttion: 
version: 
Author: Liuwen
Date: 2021-10-11 17:05:44
LastEditors: sueRimn
LastEditTime: 2021-11-17 13:20:52
'''
import requests

# 获取数据
res_music = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
json_music=res_music.json()
musci_list=json_music['data']['song']['list']
for music in musci_list:
    print(music['name'])

