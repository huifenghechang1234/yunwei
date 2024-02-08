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
异步调用多个子进程
进程池异步并发的基本使用方法
"""

'''定义子进程'''


def start_func():
    pass


def proc1():
    pass


def proc2():
    pass


if __name__ == '__main__':
    # 定义进程池，设置属性
    pool = Pool(processes=1, maxtasksperchild=2, initializer=start_func)
    # 异步启动子进程（子进程为指定的某个函数）
    pool.apply_async(proc1)
    pool.apply_async(proc2)
    # 关闭和等待子进程结束
    pool.close()
    pool.join()
