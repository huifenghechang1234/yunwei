"""
title = ''
author = 'huifenghechang'
mtime = '2024/1/13'
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
# int_num = int(11.74)
# print(type(int_num), int_num)
#
# print("整型是 %d" % int_num)  # 整型是 11

# print("1 * 1的结果是：%d" % (1 * 1))  # 1 * 1的结果是：1
# print(f"1 * 1的结果是：{1 * 1}")  # 1 * 1的结果是：1

# result = 10 > 5
# print(f"10 > 5 的结果是：{result}, 类型是{type(result)}")  # 10 > 5 的结果是：True, 类型是<class 'bool'>


# 九九乘法表
# # 定义外层循环的控制变量
# i = 1
# while i <= 9:
#
#     # 定义内层循坏的控制变量
#     j = 1
#     while j <= i:
#         # 内层循环的 print 语句，不要换行，通过\t 制表符进行对齐
#         print(f"{j} * {i}＝{j * i}\t", end='')
#         j += 1
#
#     i += 1
#     print()  # print 空内容，就是输出一个换行


# for i in range(1, 6):
#     print("语句1")
#     continue
#     print("语句2")
#
# print("***********************************************")
# for i in range(1, 6):
#     print("语句1")
#     break
#     print("语句2")




# import copy
# a = [1, 2, [3, 4]]
# b = copy.copy(a)     # 浅拷贝
#
# print(id(a[2]))      # 2081284712576
# a[2][1] = 4          # 修改a中[3, 4]元素，将3修改为4
# print(a)             # 打印结果：[1, 2, [3, 4]]
# print(b)             # 打印结果：[1, 2, [3, 4]]
# print(id(a[2]))      # 打印结果：2081284712576
# print(id(b[2]))      # 打印结果：2081284712576


def greet(name, *, greeting="Hello"):
    print(f"{greeting}, {name}!")


# 正确调用方式
greet("Alice", greeting="Hi")
# 输出: Hi, Alice!

# 错误调用方式（会抛出 TypeError）
greet("Alice", "Hi")
# TypeError: greet() takes 1 positional argument but 2 were given