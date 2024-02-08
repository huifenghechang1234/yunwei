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
threading 模块
threading模块提供Thread类和各种同步原语，用于编写多线程的程序
"""
import threading
import time


def clock(interval):
    while True:
        print("the time is %s" % time.ctime())
        time.sleep(interval)


t = threading.Thread(target=clock, args=(5,))
t.daemon = True
t.start()


