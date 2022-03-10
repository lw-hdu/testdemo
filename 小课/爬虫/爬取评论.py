import requests
from bs4 import BeautifulSoup
res=requests.get('https://wordpress-edu-3autumn.localprod.forc.work/all-about-the-future_04/')
html=res.text
bea=BeautifulSoup(html,'html.parser')
pl=bea.find_all(class_='comment-content')
#print(pl)
for i in pl:
    title=i.text
    print(title)
