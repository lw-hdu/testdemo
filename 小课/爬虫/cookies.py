'''import requests
url=' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }
data={
    'log': 'spiderman',  #写入账户
    'pwd': 'crawler334566',  #写入密码
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-admin/',
    'testcookie': '1'
    }
login=requests.post(url,headers=headers,data=data)
cookies=login.cookies
url_new='https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
data_new={
    'comment': input('请输入你想要发表的评论：'),
    'submit': '发表评论',
    'comment_post_ID': '13',
    'comment_parent': '0'
    }
pl=requests.post(url_new,headers=headers,data=data_new,cookies=cookies)
res=pl.status_code
print(res)'''


import requests
url=' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }
data={
    'log': 'spiderman',  #写入账户
    'pwd': 'crawler334566',  #写入密码
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-admin/',
    'testcookie': '1'
    }
request=requests.session()
res=request.post(url,headers=headers,data=data)
#cookies=login.cookies
url_new='https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
data_new={
    'comment': input('请输入你想要发表的评论：'),
    'submit': '发表评论',
    'comment_post_ID': '13',
    'comment_parent': '0'
    }
pl=request.post(url_new,headers=headers,data=data_new)
res=pl.status_code
print(res)