############发送json请求#########
import requests,json,time
url='http://10.221.122.91:8081/wasuicds/impCallBack'
for i in range(1,3):
    for j in range(1,3):
        data={
        "action": "0",
        "contentPlayUrl": {},
        "description": "",
        "generateContentId": j,
        "interfaceType": "",
        "processInstanceId": "",
        "result": "0",
        "sequence": i,
        "systemCode": "",
        "updatePlayUrl": "false"
         }
        res=requests.post(url,data=json.dumps(data))
    time.sleep(2)
	

import requests,json
url='http://10.221.122.91:8081/wasuicds/impCallBack'
for i in range(1,3):
#数字补0，填充左边
    id='{:0>3d}'.format(i)
    data={
        "action": "0",
        "contentPlayUrl": {},
        "description": "",
        "generateContentId": 'test_'+str(id),
        "interfaceType": "",
        "processInstanceId": "",
        "result": "0",
        "sequence": id,
        "systemCode": "",
        "updatePlayUrl": "false"
    }
#将json格式转换为字符串格式发送
    res=requests.post(url,data=json.dumps(data))
    time.sleep(2)
	
	

import requests,json,time
url='http://10.221.122.91:8081/wasuicds/impCallBack'
for i in range(1,2):
    id='{:0>3d}'.format(i)
    data={
        "action": "0",
        "contentPlayUrl": {},
        "description": "",
        "generateContentId": 'test_'+str(id),
        "interfaceType": "",
        "processInstanceId": "中文",
        "result": "0",
        "sequence": id,
        "systemCode": "",
        "updatePlayUrl": "false"
    }
    #print(json.dumps(data).encode('utf-8').decode('unicode_escape'))
    res=requests.post(url,data=json.dumps(data).encode('utf-8').decode('unicode_escape'))
    time.sleep(2)
	
	
	
#####解析json报文#####
import requests
# 引用requests库
res_music = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
# 调用get方法，下载这个字典
json_music = res_music.json()
# 使用json()方法，将response对象，转为列表/字典
list_music = json_music['data']['song']['list']
# 一层一层地取字典，获取歌单列表
for music in list_music:
# list_music是一个列表，music是它里面的元素
    print(music['name'])