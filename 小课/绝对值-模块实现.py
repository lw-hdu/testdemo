import math,time
while 1:
    time.sleep(1)
    a=input('欢迎来到绝对值计算器，按任意键继续,退出请按N\n')
    if a=='N':
        break
    else:
        num=int(input('请输入求绝对值的数：'))
        n1=math.fabs(num)
        print(str(num)+'的绝对值为'+str(n1))
        print('')