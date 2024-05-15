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
这段代码展示了如何使用APScheduler库在Python中设置定时任务。APScheduler是一个Python库，用于在给定时间、
日期或间隔后安排Python函数（或任何其他可调用的对象）的执行

cron：在特定时间定期运行 job
兼容 unix/linux 系统 crontab 格式，但是比其多了秒（second）、年（year）、第多少周（week）以及限定开
始时间（start_date）和结束时间（end_date）的功能，并且天（day）的设置更加灵活，支持类似 last fri 的格式，
具体见以下的详解。

主要参数：
year(int|str) - 年，4位数
month(int|str) - 月，1-12
day(int|str) - 日，1-31
week(int|str) - 一年中的第多少周，1-53
day_of_week(int|str) - 星期，0-6 或者 mon，tue，wed，thu，fri，sat，sun
hour(int|str) - 小时，0-23
minute(int|str) - 分，0-59
second(int|str) - 秒，0-59
start_date(date|datetime|str) - 开始时间
end_date(date|datetime|str) - 结束时间
"""
"""
导入所需库:
datetime 用于日期和时间的操作，但在这段代码中并没有直接使用。
BackgroundScheduler 是APScheduler中的一个调度器，它会在后台运行，不会阻塞主程序。
"""
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

"""
定义任务函数:
job1 是一个简单的函数，当它被调度器触发时，会打印“job1”。
job2 接受两个参数x和y，并打印它们
"""
def job1():
    print('job1')


def job2(x, y):
    print('job2', x, y)

"""
创建并启动调度器:
使用BackgroundScheduler()创建一个后台调度器实例。
调用scheduler.start()启动调度器
"""
scheduler = BackgroundScheduler()
scheduler.start()


"""
添加定时任务:
使用scheduler.add_job()方法添加任务到调度器。
每个任务都需要指定一个函数（或可调用的对象）作为任务体。
trigger 参数定义了任务的触发机制，这里使用了'cron'触发器，它允许你基于Cron表达式来设置任务的调度时间。
其他参数（如hour, minute, second, day, month, day_of_week等）用于定义Cron表达式，以指定任务的确切运行时间。
jobstore 参数定义任务存储的类型，这里使用了'mem'（内存存储）。
executor 参数定义执行任务的执行器类型，这里使用了'processpool'（进程池执行器）。
对于job2，还使用了args参数来传递额外的参数给任务函数


代码中的Cron表达式用于定义任务的执行时间，例如：
'hour=2' 表示在每天的2点运行。
'second=5, minute=30, hour=2' 表示在每天的2点30分5秒运行。
'second='*/10'' 表示每10秒运行一次。
'hour='1-3'' 表示在每天的1点、2点和3点运行。
'month='6-8,11-12', day='3rd fri', hour='1-3'' 表示在6到8月以及11到12月的第三个周五的1点、2点和3点运行。
'day_of_week='mon-fri', hour=5, minute=30, end_date='2019-12-31'' 表示在2019年12月31日之前的每周一到周五的5点30分运行
"""
# 每天 2 点运行，指定 jobstore 与 executor，默认都为 default
scheduler.add_job(
    job1,
    trigger='cron',
    hour=2,
    jobstore='default',
    executor='processpool'
)

# 每天 2 点 30 分 5 秒运行
scheduler.add_job(
    job2,
    trigger='cron',
    second=5,
    minute=30,
    hour=2,
    args=['hello', 'world']
)

# 每 10 秒运行一次
scheduler.add_job(
    job1,
    trigger='cron',
    second='*/10'
)

# 每天 1:00,2:00,3:00 运行
scheduler.add_job(
    job1,
    trigger='cron',
    hour='1-3'
)

# 在 6,7,8,11,12 月的第三个周五 的 1:00,2:00,3:00 运行
scheduler.add_job(
    job1,
    trigger='cron',
    month='6-8,11-12',
    day='3rd fri',
    hour='1-3'
)

# 在 2019-12-31 号之前的周一到周五 5 点 30 分运行
scheduler.add_job(
    job1,
    trigger='cron',
    day_of_week='mon-fri',
    hour=5,
    minute=30,
    end_date='2019-12-31'
)