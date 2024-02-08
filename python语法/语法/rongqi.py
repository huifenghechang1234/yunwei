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
5类容器的通用操作
"""
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "hello"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2}

print("******************************************************")
# len(容器)求容器内所有元素
print(f"列表元素个数是：{len(my_list)}")
print(f"元组元素个数是：{len(my_tuple)}")
print(f"字符串元素个数是：{len(my_str)}")
print(f"集合元素个数是：{len(my_set)}")
print(f"字典元素个数是：{len(my_dict)}")


print("******************************************************")
# max(容器)求容器内最大元素
print(f"列表元素最大元素是：{max(my_list)}")  # 5
print(f"元组元素最大元素是：{max(my_tuple)}")  # 5
print(f"字符串元素最大元素是：{max(my_str)}")   # o
print(f"集合元素最大元素是：{max(my_set)}")  # 5
print(f"字典元素最大元素是：{max(my_dict)}")  # key2


print("******************************************************")
# min(容器)求容器内最小的元素
print(f"列表元素最小的元素是：{min(my_list)}")  # 1
print(f"元组元素最小的元素是：{min(my_tuple)}")  # 1
print(f"字符串元素最小的元素是：{min(my_str)}")  # e
print(f"集合元素最小的元素是：{min(my_set)}")   # 1
print(f"字典元素最小的元素是：{min(my_dict)}")  # key1


print("******************************************************")
# 类型转换：容器转列表
print(f"列表转列表的结果是：{list(my_list)}")  # [1, 2, 3, 4, 5]
print(f"元组转列表的结果是：{list(my_tuple)}")  # [1, 2, 3, 4, 5]
print(f"字符串转列表的结果是：{list(my_str)}")   # ['h', 'e', 'l', 'l', 'o']
print(f"集合转列表的结果是：{list(my_set)}")  # [1, 2, 3, 4, 5]
print(f"字典转列表的结果是：{list(my_dict)}")  # ['key1', 'key2']


print("******************************************************")
# 类型转换：容器转元组
print(f"列表转元组的结果是：{tuple(my_list)}")  # (1, 2, 3, 4, 5)
print(f"元组转元组的结果是：{tuple(my_tuple)}")  # (1, 2, 3, 4, 5)
print(f"字符串转元组的结果是：{tuple(my_str)}")   # ('h', 'e', 'l', 'l', 'o')
print(f"集合转元组的结果是：{tuple(my_set)}")  # (1, 2, 3, 4, 5)
print(f"字典转元组的结果是：{tuple(my_dict)}")  # ('key1', 'key2')


print("******************************************************")
# 类型转换：容器转字符串
print(f"列表转字符串的结果是：{str(my_list)}")  # [1, 2, 3, 4, 5]
print(f"元组转字符串的结果是：{str(my_tuple)}")  # (1, 2, 3, 4, 5)
print(f"字符串转字符串的结果是：{str(my_str)}")   # hello
print(f"集合转字符串的结果是：{str(my_set)}")  # {1, 2, 3, 4, 5}
print(f"字典转字符串的结果是：{str(my_dict)}")  # {'key1': 1, 'key2': 2}


print("******************************************************")
# 类型转换：容器转集合
print(f"列表转集合的结果是：{set(my_list)}")  # {1, 2, 3, 4, 5}
print(f"元组转集合的结果是：{set(my_tuple)}")  # {1, 2, 3, 4, 5}
print(f"字符串转集合的结果是：{set(my_str)}")   # {'h', 'o', 'l', 'e'} 去重
print(f"集合转集合的结果是：{set(my_set)}")  # {1, 2, 3, 4, 5}
print(f"字典转集合的结果是：{set(my_dict)}")  # {'key1', 'key2'}  保留key


print("******************************************************")
# 容器通用排序 sorted(容器,[reverse=True]),将给定容器进行排序，排序从小到大
print(f"列表对象的排序结果是：{sorted(my_list)}")  # [1, 2, 3, 4, 5]
print(f"元组对象的排序结果是：{sorted(my_tuple)}")  # [1, 2, 3, 4, 5]
print(f"字符串对象的排序结果是：{sorted(my_str)}")  # ['e', 'h', 'l', 'l', 'o']
print(f"集合对象的排序结果是：{sorted(my_set)}")   # ['e', 'h', 'l', 'l', 'o']
print(f"字典对象的排序结果是：{sorted(my_dict)}")   # ['key1', 'key2']









