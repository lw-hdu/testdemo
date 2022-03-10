'''
Descripttion: 类练习
version: 
Author: Liuwen
Date: 2021-11-22 14:01:58
LastEditTime: 2021-11-23 13:35:25
'''
#class关键字定义一个类，类的首字母要大写
class Dog:
    def __init__(self,name,age):
        #初始化name、age，类中属性调用要带self
        self.dog_name=name
        self.dog_age=age
        self.eat='meet'
#类中定义一个方法
    def sit(self):
        print(f'the dog {self.dog_name} is sitting')

    def roll(self):
        print(f'the dog {self.dog_age} is rolling')
    #定义一个方法修改默认属性的值    
    def update_eat(self,food):
        self.eat=food
        return self.eat
#类的实例化
dog=Dog('dove','5')
#通过实例调用类的属性
print(f'my dog {dog.dog_name} is {dog.dog_age} years old,her like eat {dog.eat}')
# #调用类中的方法
dog.sit()
dog.roll()
print(dog.update_eat('beef'))

'''
类的继承
'''
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.org_miller=0
    
    def get_describe(self):
        long_name=f'{self.model} {self.make} {self.year}'
        return long_name.title()

    def update_miller(self,new_miller):
        if new_miller >= self.org_miller:
            self.org_miller =+ new_miller
        else :
            print('error')

class ElCar(Car):
    #初始化父类属性
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        #初始化子类特有属性
        self.battery_size=75

    def describe_battery(self):
        print(f'my car {self.model.title()} battery is {self.battery_size}')
#子类的实例化
elcar=ElCar('tesla','s3','2020')
#调用子类中定义的方法
elcar.describe_battery()
#调用继承的父类方法
print(elcar.get_describe())