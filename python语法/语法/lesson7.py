# -*- coding: utf-8 -*-
# @Author  : Peach
# @Phone   : 15879983825
# @Wechat  : this_zhangtao
# @File    : lesson7.py
# @Software: PyCharm
# @time    : 2022/7/24 14:07


# python中的类与对象

"""
类（class）:用来描述具有相同的属性和方法的对象的集合,它定义了该集合中每个对
象所共有的属性和方法。对象是类的实例(实际存在的例子，对象就是实例)
属性：就是变量的意思
变量的种类：
1.类变量：类变量定义在类中且在函数体（方法）之外，是有实例共有的变量，head=1,hand=2,所有人类都共有的
2.实例变量：实例特有的变量，如：小张是近视眼
方法：在类中的函数称之为方法（描述的都是动作）
1.类方法：定义在实例方法基础之上加上一个类方法的装饰器（@classmethod）
2.实例方法：实例独有的方法，只能给到实例调用
3.静态方法：需要加上一个静态方法的装饰器（@staticmethod）,是一个与类无关的函数
对象：是类当中某一个具体的实例（实际存在的例子）
实例化：根据一个类去创建不同的实例的过程
用class定义类
新式类：class People(object): ==>python3中全部默认新式类（所有的类都需要继承object）
经典类：class People: ==> 以前定义类的方法
注意点：定义类的时候，类的首字母需要大写
"""


# class People(object): # 新式类的定义方式，object是一切类的父类，基类，超级类
# 	pass

# class People: # 经典类的定义方式
# 	pass

class People(object):  # 方法/函数

    head = 1  # 类变量（所有人类共有的属性）

    def __init__(self, name, age):  # 构造方法，在给类创建实例的同时就被调用的方法，作用：起到初始化的作用 name,age是形参
        self.name = name  # 语法：self.属性名 = 属性的初始值，形参   实例属性， self.name就是实例变量,self就是实例本身
        #  第一个name是实例变量的变量名，绑定到实例化对象的属性   第二个name是形参    可以全局调用
        self.__age = age  # 属于一个私有变量，只可以在类内部访问

    def talk(self):  # self表示当前类的实例本身，talk()就是实例方法
        print(f"{self.name}可以说话")  # 在类中实例变量可以给到类中的任何一个实例调用

    def run(self):  # 实例方法
        print(f"{self.name}可以跑步")

    # 装饰器就是@符号，classmethod表示装饰的是类方法
    # 作用：在不影响原有方法的功能基础之上给原有的方法增加新的功能
    @classmethod  # 类方法装饰器
    def class_func(cls):  # cls就是class的缩写，cls表示的是当前类的本身
        print("这是一个类方法")

    @staticmethod  # 静态方法装饰器
    def static_func():
        """在类中没有任何参数的方法，静态方法，静态方法与类无关"""
        print("这是一个静态方法")

    def age_func(self):
        """获取私有变量的值，可以在类中定义实例方法用来返回__age的值
        可以在类的外部去调用age_func()方法，从而得到__age的值"""
        return self.__age  # 私有变量是可以被实例在类的内部调用

    def __owerfunc(self):  # 私有方法   私有方法是双下划线开头的方法
        print("这是一个私有方法")

    def return_ower(self):
        return self.__owerfunc()  # 在类中可以使用self实例本身去调用任何一个实例方法


if __name__ == '__main__':  # 没有使用构造方法   使用类的话必须要给类创建实例==> 需要实例化
    p = People("小张", 18)  # 给类创建一个实例p，p就是People()类中的一个实例的例子，此过程就叫实例化
    p.talk()  # 小张可以说话，通过实例p去调用People()中的实例方法talk()
    p.run()  # 小李可以跑步,通过实例p去调用People()中的实例方法run()
    #  实例调用实例方法的时候，会自动把实例传入到方法的参数self中
    People.run(p)  # 小张可以跑步   类如果要调用实例方法必须要传入实例

    #  使用了构造方法
    # 构造方法可以起到给类进行传入参数的作用
    # p = People("小张") # 在给类创建实例的同时就调用了__init__()构造方法，所以需要传入构造方法中的name参数的值
    # p.run() # 小张可以跑步
    # p.talk() # 小张可以说话

    # p1 = People("小李")
    # p1.run() # 小李可以跑步
    # p1.talk() # 小李可以说话

    # 1.类本身和对象调用（在类的外面调用）类变量
    # 类变量既可以被类调用，也可以被实例调用
    # p = People("小张")
    # print(People.head) # 1,类变量可以被类本身调用
    # print(p.head) # 1,类变量也可以被实例调用

    # 2.类本身和对象调用实例方法
    # 实例方法只能被实例调用
    # p = People("小张")
    # People.run(p) # 类如果要调用实例方法必须要传入实例，==> 实例方法不能被类调用，只能被实例调用
    # p.run() # 小张可以跑步,实例方法可以被实例调用

    # 3.类和对象调用类方法 ==> 类方法作用：可以在给类创建实例之前做一些其他准备工作
    # 使用类方法不需要实例化 ==> 是可以直接被类调用
    # 类方法既可以被类调用也可以被实例调用
    # p = People("小张")
    # People.class_func() # 这是一个类方法,类可以去调用类方法
    # p.class_func() # 这是一个类方法,实例也可以调用类方法

    # 4.类和对象调用静态方法
    # 静态方法既可以被类调用也可以被实例调用
    # p = People("小张")
    # People.static_func() # 这是一个静态方法,静态方法可以被类调用
    # p.static_func() # 这是一个静态方法,也可以被实例调用

    # 5.类中的私有变量和私有方法
    # __age是一个双下滑线开头的，全包私有变量，只能给到类本身使用
    # _age是单下划线开头的，半包私有变量，可以给到类的子类使用
    # p = People("小张",18)
    # print(p.__age) # 私有变量在类的外部是不能被任何对象所调用，只能在类中被实例调用
    print(p.age_func())  # 18，在类外部调用实例方法从而获取到私有变量的值

# 私有方法
# p = People("小张", 18)
# p.__owerfunc() # 在类外实例调用不了私有方法
# People.__owerfunc() # 在类外类调用不了私有方法
# p.return_ower() # 这是一个私有方法,在类外可以调用返回私有方法的函数进行得到私有方法的值

# 公司需要给到员工进行涨工资，涨薪的幅度为10%（所有员工），使用类进行编写
# 1.公司今年钱多，给每个员工的涨薪幅度上调到20%
# 2.对公司贡献非常大的人，涨薪30%

# class Emp(object): # 创建一个员工类
#
# 	up = 0.1 # 涨薪幅度  类变量
# 	def __init__(self,name,salary): # 构造员工的姓名及员工基本工资
# 		self.name = name
# 		self.salary = salary
#
# 	def raise_salary(self): # 定义一个涨薪的方法  实例方法
# 		self.salary = self.salary * (1 + self.up)
#
#
# if __name__ == '__main__':
# 	Emp.up = 0.2 # 在类的外面给类变量重新赋值，计算涨薪幅度就变成了20%,作用于全部员工
# 	e = Emp("小张",6000)
# 	e.raise_salary() # 通过e实例调用raise_salary()涨薪的动作
# 	print(e.salary) # 6600,涨薪之后的基本工资
#
#
# 	e1 = Emp("小李",12000)
# 	e1.up = 0.3 # 针对e1这个人的涨薪幅度上升到30%,其他人还是20%，作用是小李这个人
# 	e1.raise_salary()
# 	print(e1.salary) # 13200


# 类的三大特性 ==> 封装，继承，多态
# 1.类的封装 ==> 将类的属性及方法对外隐藏，对内可见（类的私有变量和私有方法）

# class People(object):
#
# 	def __init__(self,name):
# 		self.__name = name      # 把self.__name变量进行封装在类中，只能在类的内部进行使用
#
# 	def get_name(self):
# 		return self.__name      # 相当于在类中使用私有变量
#
# 	def __func(self):
# 		sum = 100 + 100
# 		return sum # 200
#
# 	def get_sum(self):
# 		return self.__func()
#
#
# if __name__ == '__main__':
# 	p = People("小张")
# 	print(p.get_name()) # 小张
# 	print(p.get_sum()) # 200


# 2.类的继承 ==> 子类继承父类的所有的内容,防止写多余的代码
# 父类中的私有变量以及私有方法，是不能给到子类调用的
# class Animal(object): # 定义一个动物类
#
# 	def __init__(self,name):
# 		self.name = name
#
# 	def run(self):
# 		print(f"{self.name}喜欢跑")
#
# 	def roll(self):
# 		print(f"{self.name}喜欢打滚")
#
# 	def __talk(self): # 私有方法
# 		print(f"{self.name}喜欢交流")
#
#
# class Dog(Animal):
# 	pass
#
# class Cat(Animal):
# 	pass
#
#
# if __name__ == '__main__':
# 	d = Dog("金毛") # 给Dog()创建一个对象d，需要传入父类的构造方法的参数
# 	d.run() # 金毛喜欢跑
# 	d.roll() # 金毛喜欢打滚
#
# 	c = Cat("布偶")
# 	c.roll() # 布偶喜欢打滚
# 	c.run() # 布偶喜欢跑

# Dog()类就是Animal()类的子类，Animal()是Dog()类的父类


# 3.类的多态 ==> 在某个子类中可以重写父类的方法(方法的名称需要与父类一致)，给到当前子类使用
# class Animal(object): # 定义一个动物类
#
# 	def __init__(self,name):
# 		self.name = name
#
# 	def run(self):
# 		print(f"{self.name}喜欢跑")
#
# 	def roll(self):
# 		print(f"{self.name}喜欢打滚")
#
# 	def __talk(self): # 私有方法
# 		print(f"{self.name}喜欢交流")
#
#
# class Dog(Animal):
# 	pass
#
# class Cat(Animal):
#
# 	def roll(self):
# 		print(f"{self.name}不喜欢打滚")
#
#
#
# if __name__ == '__main__':
# 	d = Dog("二哈")
# 	d.roll() # 二哈喜欢打滚
#
# 	c = Cat("狸花猫")
# 	c.roll() # 狸花猫不喜欢打滚
