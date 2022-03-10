'''
Descripttion: 文件的读写练习

with open('文件名','读写方式'，'encoding='编码格式'') as file:
    file.read()
    file.write()
 
Author: Liuwen
Date: 2021-11-22 16:15:16
LastEditTime: 2021-11-23 13:34:30
'''

'''
read,readline,readlines三者的区别
read：一次性读取整个文件内容
readline：每次读取一行内容
readlines：一次读取整个文件内容，并返回到list，供遍历使用
'''

with open(r'F:\\code\\1122\\pi_file.txt','r') as file_test: 
    # contents=file_test.readlines()
    # content=file_test.readline()
    #con=file_test.read()
    for line in file_test:
        print(line.rstrip())
    
#print(con)
# print(content)
# print(contents)

##追加写入文件
news=input('请输入要添加的内容：')
with open(r'F:\\code\\1122\\write_file.txt','a') as write_file:
    write_file.write('this is a new write file.\nnew line\n')
    write_file.write(news)


#提示用户输入名字，打印欢迎语，并把名称写入到一个文件中
while 1:
    name=input('请输入您的名字，若不想再继续，按q结束:')
    if name.lower() == 'q':
        break
    else:
        print(f'你好，{name}')
        with open(r'F:\\code\\1122\\hello.txt','a') as namefile:
            namefile.write(name+'\n')

        
        
#输入用户和喜欢的语言，并记录到文件
while True:
    name=input('请输入你的名字，不想继续按q结束：')   
    lanager=input('请输入你喜欢的语言，不想继续按q结束：') 
    if name.lower() == 'q' or lanager.lower() == 'q':
        break
    else:
        print(f'{name} faverte lanager is {lanager}')
        with open (r'F:\\code\\1122\\lanager.txt','a') as lanager_file:
            lanager_file.write(name+':'+lanager+'\n')