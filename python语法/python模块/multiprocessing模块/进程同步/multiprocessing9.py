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
进程加锁的方式
两个进程间实现同步有2种方式，1、手动加锁（释放锁）；2、with自动加锁（释放锁）
"""
# 手动加锁方式
from multiprocessing import Lock

def func():
    # 手动加锁
    Lock().acquire()

    '''执行程序'''
    pass

    # 手动释放锁
    Lock().release()


# with 自动加锁（释放锁）
from multiprocessing import Lock


def func():
    # with自动加锁（释放锁）
    with Lock():
        '''执行程序'''
        pass