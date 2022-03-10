##模拟发起post请求
import os,requests,time
url_list=[
    'http://10.221.122.90:8081/ocndb/adi2Inject?systemId=ADIPANEL',
    'http://10.221.122.89:8888/wasubo'
    ]
path=os.chdir('E:\\code\\test\\makefile-post\\xml\\testfile\\')
for url in url_list:
    for filename in os.listdir(path):
        file=open(filename,'r',encoding='UTF-8')
        xml=file.read().encode('UTF-8')
        file.close()
        #post以xml作为消息体请求时，请求正文是binary，第6行中xml为str类型，通过.encode，可以将str转为bytes
        r=requests.post(url,data=xml)
        time.sleep(2)#每隔2秒发起一个请求
print('请求发完啦')