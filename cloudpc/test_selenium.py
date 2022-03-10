from selenium import webdriver
import time

'''
dev=webdriver.Chrome()
#dev.get('http://www.baidu.com')
#获取窗口尺寸
#size=dev.get_window_size()
#print(size)
#设置窗口尺寸
dev.set_window_size(1366,768)
#打开新的标签页
new_web='window.open()'
#设置句柄（打开新的标签页）
handles=dev.window_handles
print(handles)
dev.switch_to_window('CDwindow-9990DDCFD9E4186527D1CCA47A2903EE')
#关闭当前操作浏览器
dev.close()
#关闭脚本打开的所有浏览器
dev.quit()
###打开多个浏览器并设置窗口尺寸
url_list = [{'url': 'http://www.baidu.com', 'whith': 400, 'high': 500},
            {'url': 'http://www.sougou.com', 'whith': 500, 'high': 600}]
for url in url_list:
    dev=webdriver.Chrome()
    dev.get(url['url'])#获取url并打开
    dev.set_window_size(url['whith'],url['high'])#设置窗口的大小
    time.sleep(3)
    dev.close()
dev.quit()'''

dev = webdriver.Chrome()
dev.get('http://www.baidu.com')
sougou = 'window.open("http://www.sougou.com");'

dev.execute_script(sougou)
# 获取当前页签的handle
baidu_handle = dev.current_window_handle
# 获取所有页面的handle
handles = dev.window_handles
print(handles)
for handle in handles:
    if handle != baidu_handle:
        sougou_handle = handle
dev.switch_to_window(sougou_handle)
time.sleep(5)
dev.switch_to_window(baidu_handle)


    

