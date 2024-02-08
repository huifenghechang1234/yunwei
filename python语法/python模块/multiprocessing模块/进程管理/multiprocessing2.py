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
获取子进程信息
获取子进程名称和PID
"""

import multiprocessing


def proc1():
    '''模仿一个子进程'''
    pass


def proc2():
    '''模仿一个子进程'''
    pass


if __name__ == '__main__':
    # 创建2个子进程
    p1 = multiprocessing.Process(target=proc1, name='【自定义的p1】')
    p2 = multiprocessing.Process(target=proc2)

    # 启动进程1
    p1.start()
    # 启动进程2
    p2.start()

    # 获取子进程的名称和PID
    print(f'进程1的名称为：{p1.name}, PID为：{p1.ident}')
    print(f'进程2的名称为：{p2.name}, PID为：{p2.ident}')