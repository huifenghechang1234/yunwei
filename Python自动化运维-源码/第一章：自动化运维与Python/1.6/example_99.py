# -*- coding: utf-8 -*-
#!/usr/local/bin/python
# Time: 2018/5/13 22:55:36
# Description:
# File Name: temp.py

for x in range(1, 10):  # x是乘数
    for y in range(1, x + 1):  # 主是被乘数
        print(
            f"{y}x{x}={x*y}".ljust(6), end=" "
        )  # 使用新特性f格式化字符串，也可以使用format,%等格式化，其中ljust(6)左对齐，长度为6，右补空格
    print("")  # 打印一个换行

#另一种方法
for x in range(1, 10):  # x是乘数
    for y in range(1, x + 1):  # 主是被乘数
        print(
            f"{y}x{x}={x*y:<2d}", end=" "
        )  # 使用新特性f格式化字符串，也可以使用format,%等格式化，其中ljust(6)左对齐，长度为6，右补空格
    print("")  # 打印一个换行
