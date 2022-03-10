'''
Descripttion: 模块导入练习-1
version: 
Author: Liuwen
Date: 2021-11-22 13:31:03
LastEditors: Please set LastEditors
LastEditTime: 2021-11-23 11:29:05
'''
def make_pizza(size,*foods):
    print(f'makeing a {size} pizza need the following:')
    for food in foods:
        print(f'-{food}')

