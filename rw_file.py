'''
Descripttion: 
version: 
Author: Liuwen
Date: 2021-11-11 13:12:49
LastEditors: sueRimn
LastEditTime: 2021-11-11 13:39:23
'''
with open('scores.txt','r',encoding='utf-8') as file:
    file1=file.readlines()
for i in file1:
    data=i.split()
    # print(type(data))
    sum=0
    for score in data[1:]:
        sum=sum+int(score)
    print(data[0]+':'+str(sum))
    