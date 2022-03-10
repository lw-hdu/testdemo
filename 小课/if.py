'''#!/usr/bin/python
needhelp=input('小精灵：您好，欢迎古灵阁，请问您需要帮助吗？\n')
if (needhelp == '需要'):
    choice=int(input('请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询'))
    if(choice == 1):
        print('小精灵会推荐你去存取款窗口')
    elif(choice == 2):
    	howmuch=float(input('请问您需要兑换多少金加隆呢？'))
    	print('您需要支付'+str(howmuch*31.5)+'的人民币')            
    else:
    	print('小精灵会推荐你去咨询窗口')
else:
    print('好的，再见。')'''

for i in range(1,11):
    a=input("请输入：")
    if a == "exit":
        break
    elif a == "苹果" or a=="草莓":
        continue
    #print("第"+str(i)+"次输入的是："+a)
    print("第",i,"次输入的是：",a)