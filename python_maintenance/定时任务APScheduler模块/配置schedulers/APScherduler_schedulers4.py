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
配置schedulers
在创建实例化之后再配置参数+使用配置字典参数配置
"""

# main.py

# 导入线程池执行器
from apscheduler.executors.pool import ThreadPoolExecutor
# 导入sqlalchemy，使用MySQL数据库存储
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
# 导入阻塞调度器
from apscheduler.schedulers.blocking import BlockingScheduler
# 导入cron表达式触发器
from apscheduler.triggers.cron import CronTrigger
# 导入日志模块
from loguru import logger
# 导入生成随机数模块
import random


# 创建定时任务执行函数
def my_task(number):
    logger.info("开始执行任务,传入的随机数为%s" % number)


# 实例化调度器
scheduler = BlockingScheduler()

config = {
    # 作业存储器配置 使用MySQL数据库存储
    'apscheduler.jobstores.default': {
        'type': 'sqlalchemy',
        'url': 'mysql://root:123.com@127.0.0.1:3306/job?charset=utf8'
    },
    # 执行器配置 使用线程池执行器，最大10个线程
    'apscheduler.executors.default': {
        'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
        'max_workers': '10'
    },
    # Job配置，为新任务关闭合并模式
    'apscheduler.job_defaults.coalesce': 'false',
    # Job配置，同一个任务同一时间最多只能有3个实例在运行
    'apscheduler.job_defaults.max_instances': '3',
    # Job配置，指定时区
    'apscheduler.timezone': 'Asia/Shanghai',
}
# 调度器对象配置参数
scheduler.configure(config)

if __name__ == '__main__':
    # 生成随机数传入定时任务函数
    number = random.randint(0, 9)
    # 注册定时任务job，执行频率为每分钟执行一次
    scheduler.add_job(my_task, trigger=CronTrigger.from_crontab("* * * * *"), args=[number])
    try:
        # 开始执行定时任务调度器
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logger.error("进程已结束运行")

