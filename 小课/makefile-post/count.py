'''file=open('E:\\code\\test\\makefile-post\\test.txt','w')
for i in range(1,101):
    file.write('{:0>3d}'.format(i)+'\n')
file.close()'''
print('数字补0，填充左边，宽度为2\n')
for i in range(1,11):
    num='{:0>2d}'.format(i)
    print('test_'+str(num))