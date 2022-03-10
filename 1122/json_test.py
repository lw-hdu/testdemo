'''
Descripttion: json存储数据练习
version: 
Author: Liuwen
Date: 2021-11-23 13:39:46
LastEditTime: 2021-11-23 15:34:40
'''
import json
a=['1','2','3','4']
b=json.dumps(a)
c=json.loads(b)
#打印a的类型 <class 'list'>
print(type(a))
#打印b的类型 <class 'str'>
print(type(b))
#打印c的类型 <class 'list'>
print(type(c))

#将列表a转成json格式后存入jsonfile.json文件中
#json.dump()接收两个参数，1-要存储的数据 2-用于存储参数的文件对象
with open (r'F:\\code\\1122\\jsonfile.json','w') as f:
    json.dump(a,f)

#读取json文件内容到内存中
#json.load()接收文件对象，并将其赋值给新的变量
with open (r'F:\\code\\1122\\jsonfile.json','r') as f1:
    num=json.load(f1)
    print(num)

##读取json文件中加入异常处理，
##若读取的文件存在，直接打印文件内容，若读取的文件不存在，提示输入并将输入保存到json文件
try:
    with open('F:\\code\\1122\\num.json','r') as f1:
        like_num=json.load(f1)
except FileNotFoundError:
    num_input=input('请输入你喜欢的数字：\n')
    with open('F:\\code\\1122\\num.json','w') as f:
        json.dump(num_input,f)
else:
    print(f'this is you like num:{like_num}')