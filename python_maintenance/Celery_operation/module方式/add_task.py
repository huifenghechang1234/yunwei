"""
title = ''
author = 'huifenghechang'
mtime = '2024/4/15'
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
添加任务

使用Celery异步地提交一个加法任务到任务队列，并立即得到一个表示该任务的对象，而不是等待任务完成并返回结果
"""

from celery_task import add

# 同步调用，即调用函数后，程序会等待函数执行完成并返回结果，然后继续执行后续的代码
# res=add(1, 2)  # 同步调用

# delay方法是Celery中用来异步执行任务的方法。当你调用delay方法时，你实际上是把任务提交到了任务队列（在这里可能
# 是Redis，但也可以是其他支持的broker，如RabbitMQ）。Celery的worker进程会从队列中取出任务并执行它
# delay方法会立即返回一个AsyncResult对象，而不是任务的结果。这个对象可以用来检查任务的状态、获取任务的结果等
res = add.delay(3, 4)  # 把任务提交到redis，系统返回任务uuid：b20f827d-dcf5-4fdf-a646-5abb963dc1d3

print(res)
