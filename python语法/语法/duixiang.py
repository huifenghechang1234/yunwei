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
面向对象编程
"""

class Clock:
    id = None  # 成员属性
    price = None

    def ring(self):   # 成员方法
        import winsound
        winsound.Beep(2000, 3000)
        print(f"闹钟id是:{self.id}")  # 类中调用成员属性，要加self
00

clock1 = Clock()    # 创建对象
clock1.id = "1001"   # 对象调用类的成员属性
clock1.price = "20.99"

print(f"这个闹钟的id是：{clock1.id}, 价格是：{clock1.price}")
clock1.ring()   # 对象调用类的方法

clock2 = Clock()
clock2.id = "1002"
clock2.price = "22.99"

print(f"这个闹钟的id是：{clock2.id}, 价格是：{clock2.price}")
clock2.ring()


print("*****************************************************")
# 构造方法
class Student:

    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel1 = tel
        print("Student类创建了一个类对象")

stu = Student("张三", 18, "17895556626")
print(stu.name)
print(stu.age)
print(stu.tel1)














