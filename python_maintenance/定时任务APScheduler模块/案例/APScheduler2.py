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
这段代码演示了如何使用 APScheduler 的 BlockingScheduler 来创建定时任务，并实现带参数和不带参数的函数调用
"""

from apscheduler.schedulers.blocking import BlockingScheduler


# 作业1
# 定义两个作业函数 my_job1() 和 my_job2(name)
def my_job1():
    print('hello world!')


# 作业2
def my_job2(name):
    print('hello world,', name)


"""
创建 BlockingScheduler 实例
每个五秒运行一次函数
"""
sched = BlockingScheduler()

"""
不带参数和和带有参数的函数
使用 add_job() 方法添加定时任务
"""
# 不带参数的函数，每隔 5 秒运行一次
sched.add_job(my_job1, 'interval', seconds=5)
# 带参数的函数，每隔 5 秒运行一次，参数为 'tom'
sched.add_job(func=my_job2, args=('tom',), trigger='interval', seconds=5)

# 启动调度器并运行定时任务
sched.start()
