import requests
from bs4 import BeautifulSoup
url='http://www.mtime.com/top/tv/top100/'
res=requests.get(url)
html=res.text
soap=BeautifulSoup(html,'html.parser')
print(soap.text)
#name=soap.find_all(class_='top_list')
#print(name)