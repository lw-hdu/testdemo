##模拟xview给能力系统下发计费请求
import requests,json,time,hashlib

it=int(time.time())
#print(it)
strno='xview'+str(it)+'desktops'
md5 = hashlib.md5()
b = strno.encode(encoding='utf-8')
md5.update(b)
str_md5 = md5.hexdigest()
token='xview:'+str(it)+':'+str_md5
#print(token)
n=int(input('请输入用户数：\n'))
m=int(input('请输入心跳数：\n'))

headers={
	"X-Auth-Token":token,
	"Content-Type":"application/json"
	}

def start():
    for i in range(1,n+1):
        sid='{:0>4d}'.format(i)
        surl='http://10.221.122.115:10004/accounting/'+'2020'+str(sid)
        data_fee={
        "uuid":"2020"+str(sid),
        "desktopPoolUUID":"96fd3b1aaaf711ea91d6faf905f7ea00",
        "desktopUUID":"desktopUUID"+str(sid),
        "time":it,
        "type":"0"
        }
        res_fee=requests.post(surl,data=json.dumps(data_fee),headers=headers)
        print('开始计费返回:{}'.format(res_fee.json()['result']))
    #time.sleep(0.001)
def heart():
    for x in range(1,m+1):
        for j in range(1,n+1):
            hid='{:0>4d}'.format(j)
            hurl='http://10.221.122.115:10004/accounting/'+'2020'+str(hid)
            data_heart={
                "uuid":"2020"+str(hid),
                "desktopPoolUUID":"96fd3b1aaaf711ea91d6faf905f7ea00",
                "desktopUUID":"desktopPoolUUID"+str(hid),
                "time":it,
                "type":"2"
            }
            res_heart=requests.post(hurl,data=json.dumps(data_heart),headers=headers)
            print('心跳返回：{}'.format(res_heart.json()['result']))
        time.sleep(5)
def end():
    for k in range(1,n+1):
        eid='{:0>4d}'.format(k)
        eurl='http://10.221.122.115:10004/accounting/'+'2020'+str(eid)
        data_end={
        "uuid":"2020"+str(eid),
        "desktopPoolUUID":"96fd3b1aaaf711ea91d6faf905f7ea00",
        "desktopUUID":"desktopUUID"+str(eid),
        "time":it,
        "type":"1"
        }
        res_end=requests.post(eurl,data=json.dumps(data_end),headers=headers)
        print('结束计费：{}'.format(res_end.json()['result']))

start()
time.sleep(10)
heart()
time.sleep(10)
end()