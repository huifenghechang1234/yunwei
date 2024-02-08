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
Queue 进程通信
"""
from multiprocessing import Process, Queue
from time import sleep


def proc1(q):
    '''这是一个发送消息的函数'''
    msgs = ["香蕉", "苹果", "水蜜桃"]
    for msg in msgs:
        # 将迭代对象放入通信队列
        q.put(msg)
        # 打印当前迭代的内容
        print(f"[进程1] 发送信息({msg}）")
        sleep(1)
    # 迭代完成后关闭通信
    q.close()


def proc2(q):
    '''这是一个接收消息的函数'''
    while True:
        try:
            # 删除通信队列中的一个元素
            msg = q.get(block=False)
            print(f"[进程2] 收到信息({msg}), 并删除该信息")
        except:
            q.close()  # 通信完成后关闭
            break
        sleep(1)


if __name__ == '__main__':
    # 使用Queue方法通信
    q = Queue()
    # 定义子进程属性，将 Queue 方法传入子进程
    p1 = Process(target=proc1, args=(q,))
    p2 = Process(target=proc2, args=(q,))

    # 启动2个子进程
    p1.start()
    p2.start()

    # 等待2个子进程结束
    p1.join()
    p2.join()

    print("=============== 结束 ===============")
