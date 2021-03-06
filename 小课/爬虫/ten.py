import requests
from bs4 import BeautifulSoup
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url='http://www.weather.com.cn/weather/101280601.shtml'
res=requests.get(url,headers=headers)
res.encoding='utf-8'
#print(res.text)
soap=BeautifulSoup(res.text,'html.parser')
weathers=soap.find_all(class_='wea')
tems=soap.find_all(class_='tem')
try:
    for weather in weathers:
        print('天气：'+weather.text)
    for tem in tems:
        print('温度:'+tem.text)
except AttributeError:
    pass
