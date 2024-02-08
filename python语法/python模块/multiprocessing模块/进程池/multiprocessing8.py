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
进程池的高并发
使用 map 或 imap 迭代来高效完成工作
使用 map(同步) 执行高并发。会自动等待子进程完成后，才会进行执行主进程
"""
from multiprocessing import Pool


def proc(num):
    print(f'我是子进程')


if __name__ == '__main__':
    # 定义线程池，设置并发数为5
    pool = Pool(5)
    # 使用map向函数传入多个参数(每传入一个参数则会调用一次函数，同时调用的数量由进程数决定)
    pool.map(proc, range(5))
    # 关闭进程池
    pool.close()
    print('========== 结束 ==========')



"""
使用 imap(异步) 执行高并发。调度子进程运行后不会等待，继续执行主进程任务。
若主进程运行结束，则子进程不论是否运行完成都将强制结束
"""
from multiprocessing import Pool


def proc(num):
    print(f'我是子进程')


if __name__ == '__main__':
    # 定义线程池，设置并发数为5
    pool = Pool(5)
    # 使用map向函数传入多个参数(每传入一个参数则会调用一次函数，同时调用的数量由进程数决定)
    pool.imap(proc, range(5))
    # 关闭进程池
    pool.close()
    print('========== 结束 ==========')


# 这样的好处是不会影响主进程其他任务的执行，如果需要等待则使用 join
from multiprocessing import Pool


def proc(num):
    print(f'我是子进程')


if __name__ == '__main__':
    # 定义线程池，设置并发数为5
    pool = Pool(5)
    # 使用map向函数传入多个参数(每传入一个参数则会调用一次函数，同时调用的数量由进程数决定)
    pool.imap(proc, range(5))
    # 关闭进程池
    pool.close()
    # 等待子进程结束
    pool.join()
    print('========== 结束 ==========')