'''
Author: your name
Date: 2021-11-08 11:07:25
LastEditTime: 2021-12-14 13:56:42
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \code\repet.py
'''
# students=[1,2,3,4,5]
# print(students[:2])
# students.append([3,4,5,6])
# print(students)
# source={'张三':'88','李四':'67','王五':'23'}
# print(source['张三'])
# townee = [
#     {'海底王国':['小美人鱼''海之王''小美人鱼的祖母''五位姐姐'],'上层世界':['王子','邻国公主']},
#     '丑小鸭','坚定的锡兵','睡美人','青蛙王子',
#     [{'主角':'小红帽','配角1':'外婆','配角2':'猎人'},{'反面角色':'狼'}]
#     ]
# print(townee[5][1]['反面角色'])
# movies = {
# '妖猫传':['黄轩','染谷将太'],
# '无问西东':['章子怡','王力宏','祖峰'],
# '超时空同居':['雷佳音','佟丽娅'],
# }
# actor=input('你想查询哪个演员：')
# for movie in movies:
#     actors=movies[movie]
#     if actor in actors:
#         print(actor+'出演了'+movie)


# def my_len(x):
#     count=0
#     for i in x:
#         count=count+1
#     return count

# print(my_len('张三.李,四,-王五'))
# import random
# app=['话梅花生','拍黄瓜','凉拌三丝']
# def co(fee):
#     if fee<5:
#         return(random.choice(app))
#     elif 5<fee<10:
#         return('溏心蛋',random.choice(app))

# print(type(co(3)))
# print(co(7))


# 工作时长不满六个月，发放固定奖金500元。
# 工作时长在六个月和一年之间(含一年)，发放奖金120元*月数（如8个月为960元）
# 工作时长在一年以上，发放奖金180元*月数 （如20个月为3600元）
# def money(year):
#     global price
#     if 0<year<6:
#         price=500
#     elif 6<=year<12:
#         price=120*year
#     elif year>12:
#         price=180*year
#     else :
#         price=0
#         print('请输入正确的年限')
#         return price 
# def show(n):
#     money(n)
#     print('您来公司%s年了，您的年终奖为%s'%(n,price))
# #定义类，类名首字母大写
# class Chinese:
# #定义类的属性
#     eye='黑色的'
# #创建实例的方法，不要忘了self
#     def eat(self):
#         print('使用筷子吃饭')
# #类的实例化
# chinese=Chinese()
# print('我们的眼睛是'+chinese.eye)
# chinese.eat()
# class Chinese:
#     def __init__(self,birth,live):
#         self.birth=birth
#         self.live=live
#     def b(self):
#         print('我出生在%s.'%(self.birth))
#     def l(self):
#         print('我在%s生活。'%(self.live))
#     def main(self):
#         self.b()
#         self.l()
# chinese=Chinese('阿里斯加','多伦多')
# chinese.main()
# 请用今天学到的知识创建一个机器人，让其具备以下功能：
# 一是会让你给ta 起名，也会问你的名字，然后跟你打招呼（如“你好，吴枫。我是瓦力。遇见你，真好。”）；
# 二是会让你说一个愿望，然后帮你重复三次（因为 ta 觉得重要）。
# class Rebot():
#     def __init__(self):
#         self.your_name=input('你叫什么呀？')
#     def name(self):
#         self.my_name=input('你好%s，请你给我起个名字吧：'%(self.your_name))
#         print('你好%s，我是%s，很高兴遇见你！'%(self.your_name,self.my_name))
#     def wish(self):
#         self.my_wish=input('请写下你的一个愿望：')
#         for i in range(3):
#             print('你的愿望%s一定会实现的'%(self.my_wish))
#     def main(self):
#         self.name()
#         self.wish()
# rebot=Rebot()
# rebot.main()

# to_addr=[]
# while True:
#     address=input('请输入收件箱地址：')
#     to_addr.append(address)
#     a=input('是否继续输入，n退出，任意键继续')
#     if a=='n':
#         break
# print(to_addr)

# import requests
# from bs4 import BeautifulSoup
# response=requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/')
# soap=BeautifulSoup(response.text,'html.parser')
# items=soap.find(class_='comment-list').find_all(class_='comment-body')
# for item in items:
#     I=item.find_all(class_='comment-content')
#     for i in I:
#         print(i.text)

# import requests
# from bs4 import BeautifulSoup
# url='https://wordpress-edu-3autumn.localprod.oc.forchange.cn/'
# res=requests.get(url)
# soap=BeautifulSoup(res.text,'html.parser')
# items=soap.find_all(class_='entry-header')
# for item in items:
#     pub_time=item.find(class_='entry-date published').text
#     name=item.find(class_='entry-title').text
#     link=item.find(class_='entry-title')['href']
#     print(pub_time,name,link,end=" " )


# import json
# #定义一个列表
# a=[1,2,3,4]
# #使用dumps()函数，将列表转换为json
# b=json.dumps(a)
# #打印b的类型，<class 'str'>
# print(type(b))
# #使用loads()函数，将json格式的字符串b转为列表，赋值给c
# c=json.loads(b)
# #打印c的类型，<class 'list'>
# print(type(c))
# print(c)

# a='gdyefre'
# b=1234567
# print(a+'\n'+str(b))

# current_user=['jenny','lucy','aDmin','susan','watai']
# new_user=['Susan','admin','zhangsan','lisi','wangwu']
# for new in new_user:
#     if new.lower() in current_user:
#         print(f'{new.lower()} used')
#     else:
#         print(f'you can user {new}')

# for i in range(1,10):
#     if i==1:
#         print(f'{i}st')
#     elif i==2:
#         print(f'{i}nd')
#     elif i==3:
#         print(f'{i}rd')
#     else:
#         print(f'{i}th')




# student={
#     'name':'zhangsan',
#     'sex':'male',
#     'year':'19',
# }
# #items()返回键值对
# for key,value in student.items():
#     print(f'\nkey:{key}\nvalue:{value}')
# #keys()获取所有的键,不加keys，默认获取所有的key
# for key in student.keys():
#     print(f'字典的key有{key}')
# #values()获取字典的值
# for value in student.values():
#     print(f'字典的value有{value}')

# food_list=[]
# while True:
#     food=input('请输入要添加的食材，并以quit结束：')
#     if food.lower() == 'quit':
#         break
#     else:
#         print(f'食材{food}已添加')
#         food_list.append(food)
# print(food_list)


# list1=['zhangsan','lisi','wangwu']
# list2=[]
# while list1:
#     new_list=list1.pop()
#     list2.append(new_list)
#     print(list2)

# def greet_user(names):
#     for name in names:
#         print(name)

# username=['1','2','3']
# greet_user(username)

# def user(first,last,**user_info):
#     user_info['first_name']=first
#     user_info['last_name']=last
#     print(user_info) 

# user('zhang','san',address='xa',eat='noddle')
# print(user)

# class Restant:
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
    
#     def desc(self):
#         print(f'the restant {self.name} in {self.address}')

#     def open(self):
#         print('the restant is opening')

# res=Restant('happy','xa')
# # print(f'this is my res {res.name}')
# # res.desc()
# # res.open()

# while True:
#     first_num=input('\nfirst num:')
#     if first_num == 'q':
#         break
#     second_num=input('\nsecond num:')
#     if second_num == 'q':
#         break
#     try:
#         num=int(first_num) / int(second_num)
#     except ZeroDivisionError:
#         print('除数不能为0')
#     else:
#         print(num)

import json


# num=input('请输入你喜欢的数字：\n')
# with open('F:\\code\\1122\\num.json','w') as f:
#     json.dump(num,f)
try:
    with open('F:\\code\\1122\\num.json','r') as f1:
        like_num=json.load(f1)
except FileNotFoundError:
    num_input=input('请输入你喜欢的数字：\n')
    with open('F:\\code\\1122\\num.json','w') as f:
        json.dump(num_input,f)
else:
    print(f'this is you like num:{like_num}')