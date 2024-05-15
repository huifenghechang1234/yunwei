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
终止调度器
默认情况，会终止任务存储器以及执行器，然后等待所有目前执行的job完成后（自动终止）
如果使用wait=False，不会等待任何运行中的任务完成，直接终止
1.使用默认情况，等待任务完成后终止
2.使用wait=False参数直接终止
"""
# 1.使用默认情况，等待任务完成后终止

# 导入调度器，此处使用BackgroundScheduler阻塞调度器
from apscheduler.schedulers.background import BackgroundScheduler
# 导入触发器，此处使用IntervalTrigger特定时间间隔触发
from apscheduler.triggers.interval import IntervalTrigger
# 导入日志记录器
from loguru import logger
import time


# 定时任务执行函数
def my_task():
    logger.info("开始执行task任务")
    time.sleep(2)
    logger.info("task任务执行完成")


if __name__ == '__main__':
    try:
        # 实例化调度器对象
        scheduler = BackgroundScheduler()
        # 添加定时任务，指定任务函数和触发器
        my_job = scheduler.add_job(my_task, trigger=IntervalTrigger(seconds=3))
        logger.error("开始定时任务")
        # 开始执行定时任务调度器
        scheduler.start()
        time.sleep(6)
        logger.error("终止调度器")
        scheduler.shutdown()
        logger.error(scheduler.get_jobs())
    except (KeyboardInterrupt, SystemExit):
        logger.error("进程已结束运行")





# 2.使用wait=False参数直接终止

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
    logger.info("开始执行task任务")
    time.sleep(2)
    logger.info("task任务执行完成")


if __name__ == '__main__':
    try:
        # 实例化调度器对象
        scheduler = BackgroundScheduler()
        # 添加定时任务，指定任务函数和触发器
        my_job = scheduler.add_job(my_task, trigger=IntervalTrigger(seconds=3))
        logger.error("开始定时任务")
        # 开始执行定时任务调度器
        scheduler.start()
        time.sleep(6)
        logger.error("终止调度器")
        scheduler.shutdown(wait=False)
        logger.error(scheduler.get_jobs())
    except (KeyboardInterrupt, SystemExit):
        logger.error("进程已结束运行")

