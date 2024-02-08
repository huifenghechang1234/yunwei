"""
title = ''
author = 'huifenghechang'
mtime = '2024/1/20'
code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
┏┓      ┏┓
┏┛┻━━━┛┻┓
┃      ☃      ┃
┃  ┳┛  ┗┳  ┃
┃      ┻      ┃
┗━┓      ┏━┛
┃      ┗━━━┓
┃  神兽保佑    ┣┓
┃　永无BUG！   ┏┛
┗┓┓┏━┳┓┏┛
┃┫┫  ┃┫┫
┗┻┛  ┗┻┛
"""
"""
练习
"""
from datetime import datetime

# 格式化输出

name = '周杰伦3'
age = 28

print("大家好，我是{0}，今年{1}岁".format(age, name))

name = '周杰伦2'
age = 28
print("大家好，我是{your_name}，今年{your_age}岁".format(your_name=name, your_age=age))

name = '周杰伦1'
age = 28
print("大家好，我是{0}，今年{your_age}岁".format(name, your_age=age))
print("大家好，我是{0}，今年{your_age:d}岁".format(name, your_age=age))

person = {'name': '周杰伦4', 'age': 28, 'hobby': '唱歌'}
print('大家好，我是{0[name]}，今年{0[age]}岁，我的爱好是{0[hobby]}。'.format(person))

good_percent = 98.6529
print('好评率是{}%'.format(good_percent))
print('好评率是{:.2f}%'.format(good_percent))



name = '周杰伦5'
age = 28
print(f"大家好，我是{name}，今年{age}岁")

person = {'name': '周杰伦6', 'age': 28, 'hobby': '唱歌'}
print(f'大家好，我是{person["name"]}，今年{person["age"]}岁，我的爱好是{person["hobby"]}。')


# f-string格式化还可以对date、datetime和time等时间对象进行年月日、时分秒等格式化地打印
print(f'今天是{datetime.today()}')
print(f'今天是{datetime.today():%Y-%m-%d}')
print(f'{{今天}}是{datetime.today():%Y-%m-%d}')

# 如果在f-string的花括号内填入可执行的程序语句，如计算表达式等，则在格式化时会求出其结果并填入字符串内
a = 2
b = 5
print(f'{a} × {b} = {a * b}')







