import requests
import urllib.parse
#获取验证码
photo_num=input('请输入电话号码：')
sendcode_url='https://h5.ele.me/restapi/eus/login/mobile_send_code'
header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
sendcode_data={
'captcha_hash': "",
'captcha_value': "",
'mobile':photo_num,
'scf': "ms"}
sendcode_res=requests.post(sendcode_url,data=sendcode_data,headers=header)
token=sendcode_res.json()['validate_token']#获取验证码时的token信息，登陆时会用到
#模拟登陆
request=requests.session()
login_url='https://h5.ele.me/restapi/eus/login/login_by_mobile'
login_data={
'mobile':photo_num,
'scf': "ms",
'validate_code': input('请输入验证码:'),
'validate_token': token}
login_res=request.post(login_url,data=login_data,headers=header)
#获取周边饮食
area=input('请输入你家位置：')
encode=area.encode('gbk')
keyword=urllib.parse.quote(encode)
food_url='https://www.ele.me/restapi/bgs/poi/search_poi_nearby?geohash=wqj7qgxs6k9y&keyword='+keyword+'&latitude=34.34127&limit=20&longitude=108.939842&type=nearby'
food_res=request.get(food_url,headers=header)
print(food_res.text)