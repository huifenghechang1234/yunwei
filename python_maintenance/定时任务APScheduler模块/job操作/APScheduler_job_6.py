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
修改任务触发器
如果你想重新调度一个 job （这意味着要修改其 trigger），你可以使用apscheduler.job.Job.reschedule()
或reschedule_job()方法。这些方法都会为 job 构建新的 trigger ，然后根据新的 trigger 重新计算其下一次的运行时间

1.对于使用add_job添加的任务，可以使用reschedule()方法修改任务触发器
2.通过修饰器添加的任务，可以使用reschedule_job()方法修改任务触发器
"""

# 1.对于使用add_job添加的任务，可以使用reschedule()方法修改任务触发器

# main.py
# 导入调度器，此处使用BackgroundScheduler阻塞调度器
from apscheduler.schedulers.background import BackgroundScheduler
# 导入触发器，此处使用IntervalTrigger特定时间间隔触发
from apscheduler.triggers.interval import IntervalTrigger
# 导入日志记录器
from loguru import logger
import time


# 定时任务执行函数
def my_task():
    logger.info("执行task任务")


if __name__ == '__main__':
    try:
        # 实例化调度器对象
        scheduler = BackgroundScheduler()
        # 添加定时任务，指定任务函数和触发器
        my_job = scheduler.add_job(my_task, trigger=IntervalTrigger(seconds=1))
        logger.error("开始定时任务")
        # 开始执行定时任务调度器
        scheduler.start()
        time.sleep(3)
        logger.error("修改定时任务触发器")
        my_job.reschedule(trigger=IntervalTrigger(seconds=2))
        time.sleep(3)
    except (KeyboardInterrupt, SystemExit):
        logger.error("进程已结束运行")







# 2.通过修饰器添加的任务，可以使用reschedule_job()方法修改任务触发器

# 导入调度器，此处使用BlockingScheduler阻塞调度器
from apscheduler.schedulers.background import BackgroundScheduler
# 导入触发器，此处使用IntervalTrigger特定时间间隔触发
from apscheduler.triggers.interval import IntervalTrigger
# 导入日志记录器
from loguru import logger
import time


# 实例化调度器对象
scheduler = BackgroundScheduler()


# 定时任务执行函数
@scheduler.scheduled_job(trigger="interval", seconds=1, id="my_task")
def my_task():
    logger.info("执行任务")


if __name__ == '__main__':
    try:
        logger.error("开始定时任务")
        # 开始执行定时任务调度器
        scheduler.start()
        time.sleep(3)
        logger.error("修改定时任务属性")
        scheduler.reschedule_job(job_id="my_task")
        time.sleep(3)
    except (KeyboardInterrupt, SystemExit):
        logger.error("进程已结束运行")

