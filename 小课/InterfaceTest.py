import urllib2
import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8");

def post(url):
    req=urllib2.Request(url)
    response=urllib2.urlopen(req)
    return response.read().decode("utf-8");



interfaceListFile="C:\\Python25\\test\\Interface\\interfaceList.txt"
interfaceListLog="C:\\Python25\\test\\log\\interfaceList.log"

if os.path.exists(interfaceListLog):
    os.remove(interfaceListLog)
    
f1=open(interfaceListFile,"r")
f2=open(interfaceListLog,"w")

for line in f1:
    print "Request URL:" + line + "Response:" + post(line) + "\n\n\n"
    f2.write("Request URL:" + line)
    f2.write("Response:" + post(line) + "\n\n\n")
    
f1.close()
f2.close()