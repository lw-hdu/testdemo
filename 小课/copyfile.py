import shutil 
file1='C:\\Users\\LW\\Desktop\\test\\1.txt'
path='C:\\Users\\LW\\Desktop\\test\\'
num=int(input('请输入要复制的文件数:'))
for i in range(1,num):
	file2=path+'test'+'_'+str(i)+'.txt'
	shutil.copy(file1,file2)
print('ok')