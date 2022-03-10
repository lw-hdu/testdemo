import requests
import urllib.parse
from bs4 import BeautifulSoup
name=input('请输入你想下载的电影名称：')
name_encoder=name.encode('gbk')
#quote将url中中文转换成标准的url格式
final_name=urllib.parse.quote(name_encoder)
url='http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+final_name
res=requests.get(url)
html=res.text
#将原文件转码成latin1编码（使用encode函数），再解
html_deco=html.encode("latin1").decode("gbk")
soap=BeautifulSoup(html_deco,'html.parser')
print(soap)
##############
#####quote直接使用
import requests
from bs4 import BeautifulSoup
from urllib.request import quote
name=input('请输入你想下载的电影名称：')
name_encoder=name.encode('gbk')
#quote将url中中文转换成标准的url格式
final_name=quote(name_encoder)
url='http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+final_name
res=requests.get(url)
html=res.text
#将原文件转码成latin1编码（使用encode函数），再解
html_deco=html.encode("latin1").decode("gbk")
soap=BeautifulSoup(html_deco,'html.parser')
print(soap)