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
这段代码的主要作用是定时执行 my_job() 函数，并将任务信息存储在 MongoDB 数据库中。每隔 5 秒输
出 'hello world'，直到调度器停止运行

在使用 MongoDBJobStore 时，需要提供 MongoDB 的连接信息（host、port）、集合名（collection）、
数据库名（database）、MongoClient 对象。这样 APScheduler 就会将任务信息存储在 MongoDB 中，
并在启动调度器时自动加载已存储的任务信息。

在退出应用时，通过捕获 SystemExit 异常来关闭 MongoDB 连接，确保资源的正常释放

前提：登录mongodb数据库
"""

from pymongo import MongoClient
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


# 定义任务函数 my_job()
def my_job():
    print('hello world')

# 设置 MongoDB 连接
host = '10.0.0.129'
port = 27017
client = MongoClient(host, port)

"""
配置 Job 存储后端、执行器、任务默认配置

jobstores 定义了两种 Job 存储后端：MongoDBJobStore 和 MemoryJobStore。
MongoDBJobStore 用于将任务信息存储在 MongoDB 数据库中，MemoryJobStore 
用于内存中的任务存储。

executors 定义了两种执行器：ThreadPoolExecutor 和 ProcessPoolExecutor，
分别用于线程池和进程池的任务执行。

job_defaults 设置了任务的默认配置，包括 coalesce（是否合并执行）、
max_instances（最大实例数）等
"""
jobstores = {
    'mongo': MongoDBJobStore(collection='job', database='test', client=client),
    'default': MemoryJobStore()
}
executors = {
    'default': ThreadPoolExecutor(10),
    'processpool': ProcessPoolExecutor(3)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}


"""
创建调度器 scheduler，并添加任务到调度器
创建了一个 BlockingScheduler 实例，通过 jobstores、executors 和 job_defaults 参数指定了相应的配置。
使用 scheduler.add_job() 方法添加任务 my_job，并设置触发方式为 'interval'，表示每隔 5 秒执行一次
"""
scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
scheduler.add_job(my_job, 'interval', seconds=5)

"""
启动调度器，并在捕获到 SystemExit 异常时关闭 MongoDB 连接
使用 scheduler.start() 方法启动调度器，开始执行定时任务。
通过 try-except 块捕获 SystemExit 异常，用于在应用退出时关闭 MongoDB 连接，确保资源释放
"""
try:
    scheduler.start()
except SystemExit:
    client.close()
