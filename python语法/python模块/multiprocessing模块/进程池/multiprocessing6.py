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
同步与异步并发区别
同步（阻塞）：同步并发类似于串行。例如A、B两个进程，必须A执行完成后才能执行B；若A出现
意外（一直阻塞），那么B将无法执行。
异步（非阻塞）：异步并发在执行多任务时不会出现相互阻塞的情况（进程池限制除外）。如有
A、B两个进程，他们俩可以同时进行，不会出现相互等待的情况
"""
from multiprocessing import Pool
from time import sleep


def proc1():
    '''子进程1'''
    for i in range(2):
        print(f'[进程1] 执行{i}...')
        sleep(1)


def proc2():
    '''子进程2'''
    for i in range(2):
        print(f'[进程2] 执行{i}...')
        sleep(1)


if __name__ == '__main__':
    # 定义进程池
    pool = Pool()
    # 同步执行2个子进程
    pool.apply(proc1)
    pool.apply(proc2)
    # 关闭和等待子进程结束
    pool.close()
    pool.join()
