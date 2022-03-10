import time
##创建电影注入报文
movie_file='E:\\code\\test\\makefile-post\\xml\\movie.xml'
series_file='E:\\code\\test\\makefile-post\\xml\\series.xml'
path='E:\\code\\test\\makefile-post\\xml\\testfile\\'
for i in range(5):
    now=int(time.time())
    moviefile=path+'movie-'+str(now)+'.xml'
    seriesfile=path+'series-'+str(now)+'.xml'
    fp1=open(movie_file,'r',encoding='UTF-8')#打开源文件
    fp2=open(moviefile,'w',encoding='UTF-8')#创建一个要修改的文件
    for line in fp1.readlines():#逐行读取源文件并做替换操作
        fp2.write(line.replace('${__time(yyyyMMddHHmmss)}',str(now)))
    fp1.close()
    fp2.close()
##创建电视剧注入报文
    sp1=open(series_file,'r',encoding='UTF-8')
    sp2=open(seriesfile,'w',encoding='UTF-8')
    for s in sp1.readlines():
        sp2.write(s.replace('${__time(yyyyMMddHHmm)}',str(now)))
    sp1.close()
    sp2.close()
    time.sleep(1)
    