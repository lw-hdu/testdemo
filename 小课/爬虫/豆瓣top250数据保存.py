##获取豆瓣top250并保存
##xlsx
import requests,openpyxl
from bs4 import BeautifulSoup
wb=openpyxl.Workbook()
sheet=wb.active
sheet['A1']='序号'
sheet['B1']='书名'
sheet['C1']='星级'
sheet['D1']='推荐语'
sheet['E1']='链接'
for n in range(1,11):
    page=(n-1)*25
    res=requests.get('https://movie.douban.com/top250?start='+str(page)+'&filter=')
    html=res.text
    soap=BeautifulSoup(html,'html.parser')
    movies=soap.find_all(class_='item')
    for movie in movies:
        order=movie.find('em').text
        name=movie.find(class_='title').text
        url=movie.find('a')['href']
        star=movie.find(class_='rating_num').text
        try:
            command=movie.find(class_='inq').text
        except AttributeError:
            pass
        sheet.append([order,name,star,command,url])
        #print('\n\n书名：'+name+'\n\n序号：'+order+'\n\n链接：'+url+'\n\n星级：'+star+'\n\n推荐语'+command)
wb.save('top250.xlsx')

#csv
import requests
import csv
from bs4 import BeautifulSoup
file=open('top250.csv','w',newline='',encoding='utf-8')
write_file=csv.writer(file)
write_file.writerow(['序号','书名','星级','推荐语','链接'])
for n in range(1,11):
    page=(n-1)*25
    res=requests.get('https://movie.douban.com/top250?start='+str(page)+'&filter=')
    html=res.text
    soap=BeautifulSoup(html,'html.parser')
    movies=soap.find_all(class_='item')
    for movie in movies:
        order=movie.find('em').text
        name=movie.find(class_='title').text
        url=movie.find('a')['href']
        star=movie.find(class_='rating_num').text
        try:
            command=movie.find(class_='inq').text
        except AttributeError:
            pass
        write_file.writerow([order,name,star,command,url])
        #print('\n\n书名：'+name+'\n\n序号：'+order+'\n\n链接：'+url+'\n\n星级：'+star+'\n\n推荐语'+command)
file.close()

