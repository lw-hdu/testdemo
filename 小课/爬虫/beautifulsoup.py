import requests
from  bs4 import BeautifulSoup
res=requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
html=res.text
soap=BeautifulSoup(html,'html.parser')
book=soap.find_all(class_='books')
for i in book:
    type1=i.find('h2')
    web=i.find(class_='title')
    mem=i.find(class_='info')
    print(type1.text,'\n',web.text,'\n',web['href'],'\n',mem.text)
