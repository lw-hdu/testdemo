'''
Descripttion: 
Author: Liuwen
Date: 2022-01-11 17:06:10
LastEditTime: 2022-01-12 14:51:18
'''
#列表生成式
stu = []
for i in range(1,31):
    stu.append(f'student-{i}')
print(stu)

#上边三行代码生成列表的形式可以用如下列表生成式完成，for循环后只有一行代码就可以用这种形式实现
a = [f'student-{i}' for i in range(1,31) ]
print(a)


##列表中元素去重
li = [3,5,1,5,89,13,67,55,23,78,45,13,78,3,3,3]
#先统计每个元素出现的次数，存入新的列表new
new = []
for i in li:
    #当元素个数大于1并且新列表中没有这个元素时
    if li.count(i) > 1 and [i,li.count(i)] not in new:
        new.append([i,li.count(i)])
print(new)
for j in new:
    remove_num = j[0]
    remove_cishu = j[1]
    for k in range(remove_cishu - 1):#循环删除元素的次数
        li.remove(remove_num)#删除重复的元素
print(li)


##求列表的最大最小值平均值
l3 = [3,5,1,5,89,13,67,55,23,78,45,13,78,3,3,3]
max_num = l3[0]
min_num = l3[1]
sum = 0
for i3 in l3:
    sum += i3
    if i3 > max_num:
        max_num = i3
    if i3 < min_num:
        min_num = i3
avg_num = sum / len(l3)
print(f'最大值为{max_num}，最小值为{min_num}，平均值为{avg_num}')