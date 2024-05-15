"""
title = ''
author = 'huifenghechang'
mtime = '2024/2/17'
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
使用Celery库来创建异步任务
"""

# Celery类是创建Celery应用实例的基类
from celery import Celery

# 设置了结果存储（backend）和消息中间件（broker）的URL
backend = 'redis://10.0.0.129:6379/1'  # 结果存储
broker = 'redis://10.0.0.129:6379/2'  # 消息中间件

# app=Celery(‘任务名’, broker=’xxx’, backend=’xxx’)
# 创建一个Celery应用实例，名为test。这里传入了一个字符串'test'作为应用的名称，并且设置了broker和backend的URL
app = Celery('test', broker=broker, backend=backend)  # 传一个字符串，相当于名字

"""
使用@app.task装饰器将一个普通的Python函数add转换为Celery任务。这意味着add函数现在可以被异步调用，即它可以
在后台执行，而不会阻塞调用它的代码

add函数接受两个参数a和b，然后模拟一个耗时的操作（这里使用time.sleep(3)让函数休眠3秒），最后返回两个数的和
"""


@app.task
def add(a, b):  # 很耗时的任务
    import time
    time.sleep(3)
    return a + b
