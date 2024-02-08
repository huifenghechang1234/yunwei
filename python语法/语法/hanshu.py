"""
title = ''
author = 'huifenghechang'
mtime = '2024/2/6'
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
函数进阶
"""


def test_return():
    return 1, "hello", True


x, y, z = test_return()
print(x)  # 1
print(y)  # hello
print(z)  # True

print("************************************************************")


# 多种函数传参的形式
def user_info(name, age, gender):
    print(f"姓名是：{name},年龄是：{age},性别是：{gender}")


# 位置参数（默认传参形式）
user_info('小明', 20, '男')  # 姓名是：小明,年龄是：20,性别是：男

# 关键字参数
user_info(name='小王', age=11, gender='女')  # 姓名是：小王,年龄是：11,性别是：女
user_info(age=11, name='小王', gender='女')  # 姓名是：小王,年龄是：11,性别是：女


# 可以不按照参数的顺序传参


# 默认值参数
def user_info2(name, age, gender='男'):
    print(f"姓名是：{name},年龄是：{age},性别是：{gender}")


user_info2('小王', 11)  # 姓名是：小王,年龄是：11,性别是：男
user_info2('小王', 11, '女')  # 姓名是：小王,年龄是：11,性别是：女


# 不定长参数
# 位置传递不定长, *号
def user_info3(*args):
    print(f"arg参数的类型是：{type(args)},内容是：{args}")


user_info3('Tom')  # arg参数的类型是：<class 'tuple'>,内容是：('Tom',)   元组形式


# 关键字传递不定长, **号
def user_info4(**kwargs):
    print(f"kwargs参数的类型是：{type(kwargs)},内容是：{kwargs}")


user_info4(name='Tom', age=18)  # kwargs参数的类型是：<class 'dict'>,内容是：{'name': 'Tom', 'age': 18}  字典形式

print("**************************************************************")


# 函数作为参数进行传参
"""
test函数接受一个参数compute，并在内部调用该参数作为函数来执行计算。
然后，test函数调用传递给它的compute函数，并传递了参数1和2。
所以最终输出的结果是1加2，即3
"""
def test(compute):
    result = compute(1, 2)
    print(f"compute参数的类型是：{type((compute))}")
    print(f"计算结果是：{result}")
 # return compute(1, 2)


def compute(x, y):
    return x + y


test(compute)  # compute参数的类型是：<class 'function'> 函数
               # 计算结果是：3







