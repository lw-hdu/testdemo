import requests
##获取文章内容
res=requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md')
arc=res.text
file=open('http.txt','a+')
file.write(arc)
file.close()
##获取图片
back=requests.get('https://res.pandateacher.com/2019-01-12-15-29-33.png')
pic=back.content
poto=open('pic.jpg','wb')
poto.write(pic)
poto.close()
##获取音频
res3=requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3 ')
audi=res3.content
mp3=open('test.mp3','wb')
mp3.write(audi)
mp3.close()