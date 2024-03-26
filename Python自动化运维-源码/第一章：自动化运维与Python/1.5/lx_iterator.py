# -*- coding: utf-8 -*-
#!/usr/bin/env python
# coding=utf-8


class MyList(object):  # 定义可迭代对象类

    def __init__(self, num):
        self.data = num  # 上边界

    def __iter__(self):
        return MyListIterator(self.data)  # 返回该可迭代对象的迭代器类的实例


class MyListIterator(object):  # 定义迭代器类，其是MyList可迭代对象的迭代器类

    def __init__(self, data):
        self.data = data  # 上边界
        self.now = 0  # 当前迭代值，初始为0

    def __iter__(self):
        return self  # 返回该对象的迭代器类的实例；因为自己就是迭代器，所以返回self

    def __next__(self):  # 迭代器类必须实现的方法
        while self.now < self.data:
            self.now += 1
            return self.now - 1  # 返回当前迭代值
        raise StopIteration  # 超出上边界，抛出异常

if __name__ == '__main__':
    my_list = MyListIterator(5)  # 得到一个可迭代对象
    print("使用for循环来遍历迭代器")
    for i in my_list:
        print(i)
    my_list = MyListIterator(5)  # 重新得到一个可迭代对象
    print("使用next来遍历迭代器")
    print(next(my_list))
    print(next(my_list))
    print(next(my_list))
    print(next(my_list))
    print(next(my_list))
    my_list = MyListIterator(5)  # 重新得到一个可迭代对象
    print("同时使用next和for来遍历迭代器")
    print("先使用两次next")
    print(next(my_list))
    print(next(my_list))
    print("再使用for,会从第三个元素2开始输出")
    for i in my_list:
        print(i)
