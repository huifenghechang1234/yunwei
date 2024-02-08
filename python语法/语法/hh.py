"""
title = ''
author = 'huifenghechang'
mtime = '2023/11/15'
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
# python中的类与对象
'''
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
'''

# class People(object): # 新式类的定义方式，object是一切类的父类，基类，超级类
# 	pass

# class People: # 经典类的定义方式
# 	pass

class People(object):

	head = 1 # 类变量（所有人类共有的属性）
	def __init__(self,name,age): # 构造方法，在给类创建实例的同时就被调用的方法，作用：起到初始化的作用
		self.name = name # self.name就是实例变量,self就是实例本身
		#self.__age = age # 属于一个私有变量

	def talk(self): # self表示当前类的实例本身，talk()就是实例方法
		print(f"{self.name}可以说话") # 在类中实例变量可以给到类中的任何一个实例调用

	def run(self):   # 实例方法
		print(f"{self.name}可以跑步")

	# 装饰器就是@符号，classmethod表示装饰的是类方法
	# 作用：在不影响原有方法的功能基础之上给原有的方法增加新的功能
	@classmethod  # 类方法装饰器
	def class_func(cls):  # cls就是class的缩写，cls表示的是当前类的本身
		print("这是一个类方法")

	@staticmethod  # 静态方法装饰器
	def static_func():
		'''在类中没有任何参数的方法，静态方法，静态方法与类无关'''
		print("这是一个静态方法")

	def age_func(self):
		'''获取私有变量的值，可以在类中定义个实例方法用来返回__age的值
		可以在类的外部去调用age_func()方法，从而得到__age的值'''
		return self.__age # 私有变量是可以被实例在类内的内部调用

	def __owerfunc(self):
		'''私有方法是双下划线开头的方法'''
		print("这是一个私有方法")


	def return_ower(self):
		return self.__owerfunc() # 在类中可以使用self实例本身去调用任何一个实例方法


if __name__ == '__main__':
	# 没有使用构造方法
	# 使用类的话必须要给类创建实例==> 需要实例化
	#p = People("xiaolo",12) # 给类创建一个实例p，p就是People()类中的一个实例的例子，此过程就叫实例化
	p = People()
	p.talk("小张") # 小张可以说话，通过实例p去调用People()中的实例方法talk()
	p.run() # 小李可以跑步,通过实例p去调用People()中的实例方法run()
	# 实例调用实例方法的时候，会自动把实例传入到方法的参数self中























