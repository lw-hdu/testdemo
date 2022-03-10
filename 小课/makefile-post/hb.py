import time,os,requests
def makefile():
    movie_file='E:\\code\\test\\makefile-post\\xml\\movie.xml'
    series_file='E:\\code\\test\\makefile-post\\xml\\series.xml'
    path='E:\\code\\test\\makefile-post\\xml\\testfile\\'
    num=int(input('请输入需要创建的内容个数：'))
    for i in range(num):
        now=int(time.time())
        moviefile=path+'movie-'+str(now)+'.xml'
        seriesfile=path+'series-'+str(now)+'.xml'
        fp1=open(movie_file,'r',encoding='UTF-8')
        fp2=open(moviefile,'w',encoding='UTF-8')
        for line in fp1.readlines():
            fp2.write(line.replace('${__time(yyyyMMddHHmmss)}',str(now)))
        fp1.close()
        fp2.close()
        sp1=open(series_file,'r',encoding='UTF-8')
        sp2=open(seriesfile,'w',encoding='UTF-8')
        for s in sp1.readlines():
            sp2.write(s.replace('${__time(yyyyMMddHHmm)}',str(now)))
        sp1.close()
        sp2.close()
        time.sleep(1)

def send():
    url='http://10.221.122.90:8081/ocndb/adi2Inject?systemId=ADIPANEL'
    for filename in os.listdir('E:\\code\\test\\makefile-post\\xml\\testfile'):
        file=open('E:\\code\\test\\makefile-post\\xml\\testfile\\'+filename,'r',encoding='UTF-8')
        xml=file.read().encode('UTF-8')
        file.close()
        r=requests.post(url,data=xml)
        time.sleep(5)
    print('请求发完啦')

makefile()
time.sleep(20)
send()