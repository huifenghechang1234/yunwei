"""
title = ''
author = 'huifenghechang'
mtime = '2024/1/22'
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
实现进程同步
多进程之间同步全局变量的修改，则需要使用共享内存。需要用到 multiprocessing 
模块中的 Value 共享变量类型来实现
"""
from multiprocessing import Process, Lock, Value
from time import sleep


def func1(lock, shared_var):
    for i in range(3):
        with lock:
            shared_var.value -= 1
            print(f'[func1] 共享变量var当前值为：{shared_var.value}')
            sleep(1)


def func2(lock, shared_var):
    for i in range(3):
        with lock:
            shared_var.value += 2
            print(f'[func2] 共享变量var当前值为：{shared_var.value}')
            sleep(1)


if __name__ == '__main__':
    lock = Lock()
    shared_var = Value('i', 10)

    # 定义子进程
    p1 = Process(target=func1, args=(lock, shared_var))
    p2 = Process(target=func2, args=(lock, shared_var))

    # 启动子进程
    p1.start()
    p2.start()

    # 等待子进程结束
    p1.join()
    p2.join()

    print(f'最终共享变量var为：{shared_var.value}')


# 错误示例（使用了多个 Lock() ）
from multiprocessing import Process, Lock, Value
from time import sleep


def func1(shared_var):
    '''定义子进程，让共享变量-1，执行3次'''
    for i in range(3):
        with Lock():  # 错误语句
            shared_var.value -= 1
            print(f'[func1] 共享变量var当前值为：{shared_var.value}')
            sleep(1)


def func2(shared_var):
    '''定义子进程，让共享变量+2，执行3次'''
    for i in range(3):
        with Lock():  # 错误语句
            shared_var.value += 2
            print(f'[func2] 共享变量var当前值为：{shared_var.value}')
            sleep(1)


if __name__ == '__main__':
    shared_var = Value('i', 10)

    # 定义子进程
    p1 = Process(target=func1, args=(shared_var,))
    p2 = Process(target=func2, args=(shared_var,))

    # 启动子进程
    p1.start()
    p2.start()

    # 等待子进程结束
    p1.join()
    p2.join()

    print(f'最终共享变量var为：{shared_var.value}')