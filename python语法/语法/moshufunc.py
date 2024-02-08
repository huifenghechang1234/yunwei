"""
title = ''
author = 'huifenghechang'
mtime = '2024/2/7'
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
魔术方法
"""


class Student2:

    # __init__构造方法   初始化类对象
    def __init__(self, name2, age2):
        self.name2 = name2
        self.age2 = age2

    # __str__魔术方法   控制类对象转换成字符串
    def __str__(self):
        return f"Student类对象，name:{self.name2},age:{self.age2}"

    # __lt__方法    对2个类对象进行<小于比较方法
    def __lt__(self, other):
        return self.age2 < other.age2

    # __le__方法   对2个类对象进行<=比较符号方法
    def __le__(self, other):
        return self.age2 <= other.age2

    # __eq__ 方法    对2个类对象进行==比较运算符实现方法
    def __eq__(self, other):
        return self.age2 == other.age2


stu1 = Student2("张三", 18)
stu2 = Student2("李四", 22)

# 使用__str__方法
print(stu1)  # <__main__.Student2 object at 0x000002D275B16210>  内存地址
print(str(stu1))  # <__main__.Student2 object at 0x000002D275B16210>  内存地址

# 使用__str__方法后，输出结果是Student类对象，name:张三,age:18
#                Student类对象，name:张三,age:18


# __lt__方法 使用
print(stu1 < stu2)  # True
print(stu1 > stu2)  # False

# __le__方法使用
print(stu1 <= stu2)  # True
print(stu1 >= stu2)  # False


# __eq__ 方法
print(stu1 == stu2)   # False




