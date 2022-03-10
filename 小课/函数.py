#####计算长度
def my_len(words):	
	num=0
	for i in words:	
		num=num+1
	return(num)

print(my_len('三根皮带，四斤大豆'))


#######打印盈利率
def div(num1, num2):
	gov=(num1-num2)/num2
	percent=str(gov)+'%'
	return percent

def warning():
	print('你确定上个月没有盈利吗')

def main():
	global num1
	global num2
	while 1:
		num1=int(input('请输入本月的利润'))
		num2=int(input('请输入上月的利润'))
		if num2==0:
			warning()
			continue
		else:
			print('增长率为'+div(num1,num2))
			break
main()



####计算年终奖
def low():
	return 500

def middle(year):
	money = year*120
	return money

def top(year):
	money=year*180
	return money

def main():
	while 1:
		name=input('请输入员工姓名：')
		year=float(input('请输入员工年限：'))
		if year <=0:
			print('输入年份有误，请重新输入')
			continue
		elif 0<year <=6:
			print('员工%s的年终奖为%f' %(name,low()))
		elif 12>=year>6:
			print('员工%s的年终奖为%f' %(name,middle(year)))
		else :
			print('员工%s的年终奖为%f' %(name,top(year)))
		break
main()
