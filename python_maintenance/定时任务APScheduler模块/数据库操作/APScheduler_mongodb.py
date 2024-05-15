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
APScheduler支持的数据库主要有
mongodb ：非结构化Mongodb数据库。该类型数据库经常用于对非结构化或版结构化数据的存储或操作，如 JSON
"""

# main.py
# 导入调度器，此处使用BlockingScheduler阻塞调度器
from apscheduler.schedulers.blocking import BlockingScheduler
# 导入触发器，此处使用IntervalTrigger特定时间间隔触发
from apscheduler.triggers.interval import IntervalTrigger
# 导入任务存储器，此处使用MongoDBJobStore
from apscheduler.jobstores.mongodb import MongoDBJobStore
# 导入日志记录器
from loguru import logger
# 导入MongoDB客户端
from pymongo import MongoClient


# 定时任务执行函数

def my_task():
    logger.info("开始执行任务")


if __name__ == '__main__':
    # 实例化调度器对象
    scheduler = BlockingScheduler()
    # 指定使用MongoDB存储任务
    url = 'mongodb://127.0.0.1:27017/'
    scheduler.add_jobstore(jobstore=MongoDBJobStore(client=MongoClient(host=url)))
    # 指定任务每10分钟执行一次
    scheduler.add_job(my_task, trigger=IntervalTrigger(seconds=10, timezone="Asia/Shanghai"))
    # 开始执行定时任务
    scheduler.start()

