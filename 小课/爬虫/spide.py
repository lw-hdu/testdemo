import requests
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
url='https://www.douban.com/search?q=%E4%B8%87%E7%AE%AD%E7%A9%BF%E5%BF%83'
res=requests.get(url,headers=headers)
print(res.text)