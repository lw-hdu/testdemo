'''
Descripttion: 
Author: Liuwen
Date: 2022-01-24 14:01:54
LastEditTime: 2022-01-24 14:31:11
'''
i=1
g = 178
print(f'第1年的值为：{g}')
while i < 25:
    n = g - g * 0.0045
    g = n
    i += 1
    print(f'第{i}年的值为：{n}')
