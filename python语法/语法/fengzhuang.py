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
封装
"""


class Animal:
    id = 1

    def speak(self):
        print("Animal speaks")


class Dog(Animal):  # 子类Dog继承父类Animal
    def bark(self):
        print("Dog barks")

    def speak(self):  # 子类复写父类
        print("狗叫")

        # 子类调用父类属性和方法
        # 方法1
        print(f"父类的id是：{Animal.id}")  # 子类调用父类成员属性
        Animal.speak(self)  # 子类调用父类方法

        # 方法2
        print(f"父类的id是：{super().id}")
        super().speak()


class Cat(Animal):
    def meow(self):
        print("Cat meows")


# 创建 Dog 对象
dog = Dog()
dog.speak()  # 输出 "Animal speaks"
dog.bark()  # 输出 "Dog barks"

print("**************************************")
# 创建 Cat 对象
cat = Cat()
cat.speak()  # 输出 "Animal speaks"
cat.meow()  # 输出 "Cat meows"
