"""
title = ''
author = 'huifenghechang'
mtime = '2024/1/20'
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
multiprocessing模块是Python标准库中提供的一个用于实现多进程编程的模块。
它基于进程而不是线程，可以利用多核CPU的优势，提高程序的执行效率，同时也可以
实现进程间通信和数据共享
"""

# Process（控制进程）
# 用于创建子进程对象，必须指定要执行的目标函数。Process(target = [函数名])

"""
判断子进程状态
通过 is_alive 判断某个子进程是否存活
"""

import multiprocessing
from time import sleep


# 定义一个函数(作为子进程)
def proc():
    print('=========== 子进程开始运行 ===========')
    sleep(3)
    print('=========== 子进程运行结束===========')


if __name__ == '__main__':
    # 将函数proc定义为子进程
    p = multiprocessing.Process(target=proc)

    # 启动子进程
    p.start()

    # 判断子进程是否结束
    while p.is_alive():
        print('[CHECK] 子进程运行中')
        sleep(1)
    else:
        print('子进程已死亡！')
