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
强制杀死子进程
通过 terminate 或者 kill 强制杀死子进程
"""
import multiprocessing
from time import sleep


# 定义2个函数(作为子进程)
def proc1():
    print('=========== 子进程1开始运行 ===========')
    sleep(10)
    print('=========== 子进程1运行结束===========')


def proc2():
    print('=========== 子进程2开始运行 ===========')
    sleep(10)
    print('=========== 子进程2运行结束===========')


if __name__ == '__main__':
    # 将函数定义为子进程
    p1 = multiprocessing.Process(target=proc1)
    p2 = multiprocessing.Process(target=proc2)

    # 启动子进程
    p1.start()
    p2.start()

    # 3秒后手动杀死子进程
    sleep(3)
    p1.kill()  # 使用kill杀死子进程
    p2.terminate()  # 使用terminate杀死子进程
    print('子进程p1、p2已被强制杀死！')