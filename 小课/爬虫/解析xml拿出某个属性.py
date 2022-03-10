from bs4 import BeautifulSoup
import lxml
import os
for filename in os.listdir('E:\\code\\xml\\'):
    #print(filename)
    file=open('E:\\code\\xml\\'+filename,'r',encoding='UTF-8')
    xml=file.read()
    soap=BeautifulSoup(xml,'lxml')
    #print(soap)
    video=soap.find('adi:acceptcontentasset').find('vod:video')['transfercontenturl']
    print(video)
