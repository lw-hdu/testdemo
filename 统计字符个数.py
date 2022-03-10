'''
Descripttion: 
Author: Liuwen
Date: 2022-01-11 15:23:18
LastEditTime: 2022-01-11 15:53:15
'''
while True:
    msg = input('请输入要统计的内容，若不再输入，以n结束：\n')
    if msg.lower() == 'n':
        break
    elif len(msg) == 0:
        continue
    str_num = 0
    int_num = 0
    space_num = 0
    specila_num = 0
    for i in msg:
        if i.isalpha():
            str_num += 1
        elif i.isdigit():
            int_num += 1
        elif i.isspace():
            space_num += 1
        else:
            specila_num += 1
    print(f'str_num is {str_num},int_num is {int_num},space_num is {space_num},special_num is {specila_num}')


