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
子进程执行多任务
实现简单的多任务执行
"""

import multiprocessing
import time


def progress1():
    '''模仿一个子进程'''
    for i in range(1, 6):
        print(f'[{i}/5] 这是进程1，每隔1s输出一次...')
        time.sleep(1)


def progress2():
    '''模仿一个子进程'''
    for i in range(1, 5):
        print(f'[{i}/4] 这是进程2，每隔2s输出一次...')
        time.sleep(2)


if __name__ == '__main__':
    # 创建2个子进程
    p1 = multiprocessing.Process(target=progress1)
    p2 = multiprocessing.Process(target=progress2)

    # 启动进程1
    p1.start()
    # 启动进程2
    p2.start()

    # 程序执行其他事情
    time.sleep(1)
    print('=============== 结束 =============== ')