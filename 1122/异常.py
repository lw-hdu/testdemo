'''
Descripttion: 异常处理练习

try:
    XXXX
except:
    异常提示或pass
else：
    未发生异常时执行语句

version: 
Author: Liuwen
Date: 2021-11-23 11:29:43
LastEditTime: 2021-11-23 13:34:37
'''

#练习一：获取文件中的字数，文件不存在时抛出异常
def count(filename):
    try:
        path='F:\\code\\1122\\'
        with open (path+filename,encoding='utf-8') as f:
            content=f.read()
            #split()用于将读取内容以空格分隔，列表数据返回
            words=content.split()
            count=len(words)
    except FileNotFoundError:
        pass #pass在此处充当占位符
        #print(f'the file {filename} is not in')
    else:
        print(f'{filename} have {count} words')

filename_list=['alice.txt','little_women.txt','lion king.txt']
for file in filename_list:
    count(file)

##练习二：数字求和，输入非数字时抛出异常
while 1:

    num1=input('\n请输入第一个数字：')
    if num1 == 'q':
        break
    num2=input('\n请输入第二个数字：')
    if num2 == 'q':
        break
    try:
        sum=float(num1)+float(num2)
    except ValueError:
        pass
        #print('请输入数字类型')
    else:
        print(f'{num1}和{num2}相加的和为{sum}')