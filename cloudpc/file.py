#写文件
fw=open('‪test.txt','a',encoding='utf-8')
fw.write('张三\n李四\n王五789\n')
fw.close()
#read读文件
fr=open(r'E:\code\‪test.txt','r',encoding='utf-8')
fr_str=fr.read()
print('read函数的返回值:\n{}'.format(fr_str))
fr.close()
#readline读文件
frl=open(r'E:\code\‪test.txt','r',encoding='utf-8')
frl_list=frl.readline()
print('\nreadline函数的返回值:\n{}'.format(frl_list))
frl.close()
#readlines读文件
frls=open(r'E:\code\‪test.txt','r',encoding='utf-8')
frls_list=frls.readlines()
print('\nreadlines函数的返回值:\n{}'.format(frls_list))
frls.close()
##with方式不需要手工关闭文件
with open('‪with_test.txt','a',encoding='utf-8') as file:
    file.write('decrwrfrwfrfrrr\n张萨达维尔法')

with open(r'E:\code\‪with_test.txt','r',encoding='utf-8') as filer:
    print(filer.readlines())