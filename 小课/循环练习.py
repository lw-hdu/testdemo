#for方式
for i in range(5):
    a = int(input('请输入0结束循环，你有5次机会:'))
    if a == 0:
        print('你触发了break语句，导致else语句不会生效。')    
        break
else:
    print('5次循环你都错过了，else语句生效了。')

for i in range(5):
	a=int(input('输入0结束循环'))
	if a!=0:
		continue
	else:
		print('5次机会都错过了')
		break


#while方式  
i=0     
while i < 5:
	a=int(input('请输入0结束循环，你有5次机会:'))
	i=i+1
	if(a==0):
		print('你触发了break语句，导致else语句不会生效。')
		break
else:
	print('5次循环你都错过了，else语句生效了。')

##猜数字，不限制次数
while 1:
	i=int(input('请输入你猜的数值：'))
	if i<24:
		print('你猜的太小啦')
	elif i>24:
		print('你猜的太大啦')
	else:
		print('恭喜你猜对啦')
		break

##猜数字，限制次数
a=0
while a<3:
	i=int(input('请输入你猜的数值：'))
	a=a+1
	if i<24:
		print('你猜的太小啦')
	elif i>24:
		print('你猜的太大啦')
	else:
		print('恭喜你猜对啦')
		break
else:
	print('没机会了')


for i in range(3):
	a=int(input('请输入你猜的数值：'))
	if a<24:
		print('小了')
	elif a>24:
		print('大了')
	else:
		print('答对了')
		break
else:
	print('你没机会了')


##打印判决
while 1:
	a=input('请a输入你的选择：')
	b=input('请b输入你的选择：')

	if a=='抵赖' and b=='抵赖':
		print('各判3年')
		break
	elif a=='认罪' and b=='抵赖':
		print('a判1年，b判10年')
	elif a=='抵赖' and b=='认罪':
		print('a判10年，b判1年')
	else:
		print('各判10年')

##登录测试
#for方式
for i in range(3):
    name=input('请输入用户名：\n')
    passwd=input('请输入密码：\n')
    if name=='abc' and passwd='123':
        print('登录成功')
        break#####登录成功，跳出循环，如果不加这句，即使第一次输入成功，也要走3遍循环
    else:
        print('输入有误，请重新输入')
        continue###回到循环开头，重新开始循环
else:###循环结束，输出结果，如果不加else，即使第一次输入成功，也会打印“没机会了”，此处的else与for同级，当i不在0-2范围时，才会打印
    print('没机会了')

#while方式
n=0
while n<3:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == 'abc' and password == '123':
        print("登录成功")
        break
    else:
        n=n+1
        print("输入有误")
else:
    print("你输错了三次，登录失败")