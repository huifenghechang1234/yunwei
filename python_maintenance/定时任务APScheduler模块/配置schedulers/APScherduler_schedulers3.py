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
在创建实例化之后再配置参数+将关键字参数传递配置
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

# 作业存储器配置 使用MySQL数据库存储
url = 'mysql://root:123.com@127.0.0.1:3306/job?charset=utf8'

#
executors = {
    'default': ThreadPoolExecutor(10),
}
# Job相关配置，更多选项参见官方文档
job_defaults = {
    'coalesce': False,
    # 设置这个目的是，比如由于某个原因导致某个任务积攒了很多次没有执行（比如有一个任务是1分钟跑一次，但是系统原因断了5分钟），
    # 如果 coalesce=True，那么下次恢复运行的时候，会只执行一次，而如果设置 coalesce=False，那么就不会合并，会5次全部执行
    'max_instances': 3
    # 同一个任务同一时间最多只能有3个实例在运行。
    # 比如一个10分钟的job，指定每分钟运行1次，如果max_instance=3，那么在第3~10分钟上，新的运行实例不会被执行，因为已经有3个实例在运行。
}
# 调度器对象配置参数
scheduler.configure(
    job_defaults=job_defaults,
    timezone='Asia/Shanghai')
# 添加任务存储器参数
scheduler.add_jobstore(jobstore=SQLAlchemyJobStore(url=url))
# 添加执行器参数,使用线程池执行器，最大10个线程
scheduler.add_executor(executor=ThreadPoolExecutor(max_workers=10))

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

