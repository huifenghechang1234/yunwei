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
Pipe 管道通信
        Pipe()支持多个进程间的管道通信。管道可以被多个进程访问，但是一次只能有一个进程对管道进行操作。
        Pipe()赋值给两个对象：p1,p2 = Pipe()，p1是发送消息的方法，p2是接收消息的方法
"""
# 定义2个进程，分别向管道中发送消息和接收消息
from multiprocessing import Pipe, Process


class MyClass(object):
    '''定义2个管道和2个进程，相互发送和接收消息'''

    def __init__(self):
        # parent_conn表示发送消息，child_conn表示接收消息
        self.parent_conn1, self.child_conn1 = Pipe()
        self.parent_conn2, self.child_conn2 = Pipe()

    def proc1(self):
        # 向管道1中发送消息
        self.parent_conn1.send('苹果')
        # 接收管道2中的消息
        received_message = self.child_conn2.recv()
        print(f'[进程1] 收到的消息是：{received_message}')
        # 关闭管道1
        self.parent_conn1.close()

    def proc2(self):
        # 接收管道1中的消息
        received_message = self.child_conn1.recv()
        print(f'[进程2] 收到的消息是：{received_message}')
        # 向管道2中发送消息
        self.parent_conn2.send('香蕉')
        # 关闭管道2
        self.parent_conn2.close()


if __name__ == '__main__':
    mc = MyClass()

    # 创建子进程
    p1 = Process(target=mc.proc1)
    p2 = Process(target=mc.proc2)

    # 启动子进程
    p1.start()
    p2.start()

    # 等待子进程结束
    p1.join()
    p2.join()

    print('=================== 结束 ===================')