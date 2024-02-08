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
运行多个并发
通过循环的方式去构造多个并发
"""

import multiprocessing
from time import sleep


class MyClass(object):
    def __init__(self, thread_num=1, sleep_proc=None):
        # thread_num表示进程数，sleep_proc表示是否等待退出
        self.thread_num = thread_num
        self.sleep_proc = sleep_proc

    def proc(self):
        # 定义一个并发的子进程
        for i in range(1, 4):
            print(f'[{i}/3] 我是一个子进程')
            sleep(1)

    def call_proc(self):
        # 调用子进程
        processes = []
        # 循环调用多个子进程
        for num in range(self.thread_num):
            # 定义子进程属性
            p = multiprocessing.Process(target=MyClass().proc)
            # 启动子进程
            p.start()
            # 将循环的子进程放入列表，用于后面的等待退出
            processes.append(p)

        # 判断是否等待子进程结束
        if self.sleep_proc is True:
            for p in processes:
                p.join()


if __name__ == '__main__':
    # 指定2个并发，并等待子进程结束
    mc = MyClass(2, True)
    mc.call_proc()

    print('=============== 结束 ===============')

