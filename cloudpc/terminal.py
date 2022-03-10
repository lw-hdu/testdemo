##模拟客户端给南向网关发消息
import requests,json,time,hashlib,random

delay=random.randint(1,50)
it=int(time.time())
strno='xview'+str(it)+'desktops'
md5 = hashlib.md5()
b = strno.encode(encoding='utf-8')
md5.update(b)
str_md5 = md5.hexdigest()
token='xview:'+str(it)+':'+str_md5

headers={
	"X-Auth-Token":token,
	"Content-Type":"application/json"
	}
headers_notoken={
	"Content-Type":"application/json"
	}

def req():
	for i in range(3,10):
		sid='{:0>4d}'.format(i)
		req_url='http://10.221.122.115:10003/terminal/command'
		data_req={
			"command":"apply_command",
			"system":"other",
			"taskId":"2020"+str(sid),
			"userUuid":["2020"+str(sid)],
			"data":{
				}
			}
		res_req=requests.post(req_url,data=json.dumps(data_req),headers=headers_notoken)

def back():
	for j in range(3,10):
		sjd='{:0>4d}'.format(j)
		back_url='http://10.221.122.115:10004/channel'
		data_back={
			"type":5,
			"data":{
				"command":"apply_command", 
				"system":"other",   
				"taskId":"2020"+str(sjd),
				"userUuid":"2020"+str(sjd),
				"resultCode":"error",
				"resultMsg":"2020"+str(sjd)+"失败",
			"data":{
				}
			}
		}
		res_back=requests.post(back_url,data=json.dumps(data_back),headers=headers)

def report():
	report_url='http://10.221.122.115:10004/channel'
	data_report={
		"type":6,
		"data":{
			"command":"HEARTBEAT_COMMAND", 
			"userUuid":"22222",   
		"data":{
            "appVersion":"1.0.0.2",
            "machineType":"A2000",
            "machineNum":"123588",
            "networkDelay":delay
			}
	}
}
	res_end=requests.post(report_url,data=json.dumps(data_report),headers=headers)

#back()
#report()
#time.sleep(5)
report()
#req()
#time.sleep(2)
#back()