'''
Author: your name
Date: 2021-11-04 16:36:11
LastEditTime: 2021-11-05 11:09:51
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \code\sql.py
'''
import pymysql
from pymysql.cursors import Cursor
#查询数据库检查创建是否成功
#name='test_helium'
connection=pymysql.connect(db='monitor',user='root',password='123456',host='10.0.10.130',port=3306,autocommit=True)
cursor=connection.cursor()
cursor.execute("SELECT * FROM mon_user where login_name='%s'" %('liuwen'))
result=cursor.fetchall()
print(result)
connection.close()