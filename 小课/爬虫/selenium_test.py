'''# 本地Chrome浏览器设置方法
from selenium import  webdriver 
import time

driver = webdriver.Chrome() 
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') 
time.sleep(2)

teacher = driver.find_element_by_id('teacher')
teacher.send_keys('必须是吴枫呀')
teacher.clear()
time.sleep(1)
teacher.send_keys('吴峰')
assistant = driver.find_element_by_name('assistant')
assistant.send_keys('都喜欢')
time.sleep(1)
button = driver.find_element_by_class_name('sub')
time.sleep(1)
button.click()
time.sleep(1)
driver.close()'''

'''from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver=webdriver.Chrome()
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') # 访问页面
time.sleep(2) # 等待2秒
#lables=driver.find_elements_by_tag_name('label')
#print(lables)
#for lable in lables:
#    print(lable.text)
pageSource=driver.page_source
soap=BeautifulSoup(pageSource,'html.parser')
driver.close() 

from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php')
time.sleep(2)
name =driver.find_element_by_id('user_login')
name.send_keys('spiderman')
passwd=driver.find_element_by_id('user_pass')
passwd.send_keys('crawler334566')
butt=driver.find_element_by_class_name('button')
butt.click()
arc=driver.find_element_by_link_text('未来已来（三）——同九义何汝秀')
time.sleep(2)
arc.click()
time.sleep(2)
content=driver.find_element_by_id('comment')
content.send_keys('selenium测试已下线')
butt1=driver.find_element_by_class_name('submit')
butt1.click()
driver.close()'''


'''from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from bs4 import BeautifulSoup
import time
chrome_options=Options()
chrome_options.add_argument('--headless')
driver=webdriver.Chrome(options = chrome_options)
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/show')
pageSource=driver.page_source
soap=BeautifulSoup(pageSource,'html.parser')
#print(soap)
contents=soap.find_all(class_='content')
for content in contents:
    #print(type(content))
    arc=content.find(id='p').text
    print(arc)
    time.sleep(1)

driver.close()'''


from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from bs4 import BeautifulSoup
import time
chrome_options=Options()
chrome_options.add_argument('--headless')
driver=webdriver.Chrome(options = chrome_options)
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)
teacher = driver.find_element_by_id('teacher')
teacher.send_keys('必须是吴枫呀')
assistant = driver.find_element_by_name('assistant')
assistant.send_keys('都喜欢')
time.sleep(1)
button = driver.find_element_by_class_name('sub')
time.sleep(1)
button.click()
time.sleep(2)
contents=driver.find_elements_by_class_name('content')
for content in contents:
    arc=content.text
    print(arc)
driver.close()

