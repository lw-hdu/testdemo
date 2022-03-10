'''
Descripttion: 发送邮件练习
version: 
Author: Liuwen
Date: 2021-11-11 11:39:31
LastEditors: Please set LastEditors
LastEditTime: 2021-12-15 11:27:21
'''
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header

def send_email():
    # from_addr=input('请输入邮箱用户名：')
    # password=input('请输入邮箱授权码：')
    curtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    to_addr=[]
    while True:
        address=input('请输入收件箱地址：')
        to_addr.append(address)
        a=input('是否继续输入，n退出，任意键继续')
        if a=='n':
            break

    # from_addr='lw_hdu@163.com'
    # password='ZXFOMKFKOXDDTGYJ'
    # to_addr=['liuwen10@longi.com','1522007934@qq.com']
    smtp_server='smtp.163.com'
    #邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    text=f'您好，现在是{curtime}，今天也要加油呦！'
    msg=MIMEText(text,'plain','utf-8')
    #邮件头信息
    msg['From']=Header('lw_hdu@163.com')
    msg['To']=Header(','.join(to_addr))
    msg['Subject']=Header(curtime+'   python测试发送邮件')
    #开启发信服务
    server=smtplib.SMTP()
    server.connect(smtp_server,25)
    #登录邮箱
    server.login('lw_hdu@163.com','ZXFOMKFKOXDDTGYJ')
    #发送邮件
    server.sendmail('lw_hdu@163.com',to_addr,msg.as_string())
    #关闭服务器
    server.quit()

if __name__ == '__main__':
    send_email()
