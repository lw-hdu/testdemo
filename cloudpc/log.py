import os
def hebing():
    #列出要合并的文件名
    loglist=os.listdir('E:\\code\\log')
    #创建一个新文件用户写合并后文件
    temp=open('E:\\code\\log\\temp.log','w',encoding='UTF-8')
    #新文件中写数据
    for log in loglist:
        oldlog=open('E:\\code\\log\\'+log,'r',encoding='UTF-8')
        temp.write(oldlog.read())
        oldlog.close()
    temp.close()


def paixu():
    #将文件转换成字典
    loglists=[]#空列表
    logmap={}
    logmaps={}
    newlines=open('E:\\code\\log\\temp.log','r',encoding='UTF-8')#打开合并后文件
    for newline in newlines.readlines():
        key=newline.split(' ',1)#将合并文件用空格分割，生成列表
        loglists.append(key)
    for loglist in loglists:
        logmap={loglist[0]:loglist[1:len(loglist)]}#将列表中的第一个元素作为key，剩余元素作为value生成字典
        logmaps.update(logmap)#字典合并
    #排序并生成新文件
    for log in sorted(logmaps):#字典排序
        a=log,logmaps[log]
        #print(a)
        newlog=open('E:\\code\\log\\newlog.log','a',encoding='UTF-8')#将打印信息写到文件中
        print(a,file=newlog)
        #newlog2.write(str(a))
    newlog.close()

hebing()
paixu()







