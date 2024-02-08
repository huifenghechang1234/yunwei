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
Queue 控制多个子进程
设置多个子进程，一个用于控制，其他执行对应程序
控制的方法：运行子进程通过消息队列判断是否继续运行。
若消息队列为空，继续运行子进程；若消息队列不为空，停止子进程。由控制子进程决定
"""
from multiprocessing import Process, Queue
from time import sleep


class MyClass(object):
    def __init__(self, time):
        self.time = time  # 指定n秒后退出子进程
        self.q = Queue()  # 将Queue赋值给公共方法

    def sed_msgs(self):
        '''该方法决定子进程是否退出'''
        sleep(self.time)  # 按指定时间休眠
        self.q.put('over')  # 休眠后向消息队列发送一条消息
        self.q.close()  # 关闭通信

    def proc1(self):
        '''这是一个子进程，当消息队列不为空则停止运行'''
        while self.q.empty():
            print('[进程1] 执行当前任务...')
            sleep(1)
        self.q.close()

    def proc2(self):
        '''这是一个子进程，当消息队列不为空则停止运行'''
        while self.q.empty():
            print('[进程2] 执行当前任务...')
            sleep(1)
        self.q.close()


if __name__ == '__main__':
    mc = MyClass(3)  # 给定休眠时间3s

    # 定义子进程
    s1 = Process(target=mc.sed_msgs)
    p1 = Process(target=mc.proc1)
    p2 = Process(target=mc.proc2)
    communication = [s1, p1, p2]

    # 启动所有子进程
    for s in communication:
        s.start()

    # 等待所有子进程结束
    for s in communication:
        s.join()

    print('====================== 结束 ======================')