##csv方式存文件
#写csv文件
import csv
#加newline=''是为了避免csv文件中出现空行
file=open('test.csv','w',newline='',encoding='utf-8')
#调用csv.writer()函数创建一个write_file对象
write_file=csv.writer(file)
write_file.writerow(['电影','评分'])
write_file.writerow(['美国队长','8.0'])
write_file.writerow(['狮子王','9.4'])
file.close()
#读csv文件
rfile=open('test.csv','r',encoding='utf-8')
#调用csv.reader()函数创建一个read_file对象
read_file=csv.reader(rfile)
for i in read_file:
    print(i)
