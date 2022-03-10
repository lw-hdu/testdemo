from selenium import webdriver
import time
dev=webdriver.Chrome()
dev.get('http://114.215.144.4:9090/mtx/')
'''login_button=dev.find_element_by_xpath('/html/body/div[2]/div/ul[1]/div/div/a[1]')
login_button.click()'''
login_button=dev.find_elements_by_link_text('登录')
login_button[0].click()
login_text=dev.find_element_by_xpath('//*[@placeholder="用户名/手机/邮箱"]')
login_text.send_keys('lwww')
time.sleep(2)
passwd_text=dev.find_element_by_xpath('//*[@placeholder="登录密码"]')
passwd_text.send_keys('123456')
time.sleep(2)
login_button2=dev.find_element_by_xpath('//*[text()="登录" and @type="submit"]')
login_button2.click()

dev.close()
