# -*- coding: utf-8 -*-


def myList(num):  # 定义生成器
    now = 0  # 当前迭代值，初始为0
    while now < num:
        val = (yield now)  # 返回当前迭代值，
        now = now + 1 if val is None else val  # val为None，迭代值自增1，否则重新设定当前迭代值为val


my_list = myList(5)  # 得到一个生成器对象
print("for 循环遍历生成器myList")
for i in my_list:
    print(i)

my_list = myList(5)  # 得到一个生成器对象
print("next遍历生成器myList")
print(next(my_list))  # 返回当前迭代值值
print(next(my_list))  # 返回当前迭代值值
print(next(my_list))  # 返回当前迭代值值
print(next(my_list))  # 返回当前迭代值值
print(next(my_list))  # 返回当前迭代值值
