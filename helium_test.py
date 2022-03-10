'''
Author: your name
Date: 2021-11-04 09:39:32
LastEditTime: 2021-11-10 08:29:42
LastEditors: sueRimn
Description: In User Settings Edit
FilePath: \code\helium_test.py
'''

from helium import *
from time import sleep
import pymysql
from pymysql.cursors import Cursor
start_chrome('http://10.0.10.131/')
write('admin',into="请输入用户名")
#press(TAB)
write('1qaz!QAZ',into="请输入密码")
press(ENTER)
sleep(3)
# click("账号管理")
# sleep(2)
# click("LW企业")
# click("添加")
# sleep(2)
# write('test_helium',into='用户名')
# press(TAB)
# write('测试helium')
# sleep(2)
# write('123456',into='密码')
# sleep(2)
# press(TAB)
# press(TAB)
# press(ENTER)
kill_browser()
# #查询数据库检查创建是否成功
# connection=pymysql.connect(db='monitor',user='root',password='123456',host='10.0.10.130',port=3306,charset='utf-8')
# cursor=connection.cursor()
# cursor.execute("SELECT * FROM mon_user WHERE login_name='%s'" %('test_helium'))
# result=cursor.fetchone()
# print(result)
# connection.close()