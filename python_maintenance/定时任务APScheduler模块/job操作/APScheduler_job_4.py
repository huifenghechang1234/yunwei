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
暂停/恢复任务
通过Job实例或者 scheduler 本身你可以轻易地暂停和恢复 job 。当一个 job 被暂停，它的下一次
运行时间将会被清空，同时不再计算之后的运行时间，直到这个 job 被恢复。

1.对于使用add_job添加的任务，可以使用pause()方法暂停任务，使用resume()方法恢复任务
2.通过修饰器添加的任务，可以使用pause_job()方法暂停任务，使用resume_job()方法恢复任务
"""

# 1.对于使用add_job添加的任务，可以使用pause()方法暂停任务，使用resume()方法恢复任务

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
    logger.info("执行任务")


if __name__ == '__main__':
    try:
        # 实例化调度器对象
        scheduler = BackgroundScheduler()
        # 添加定时任务，指定任务函数和触发器
        my_job = scheduler.add_job(my_task, trigger=IntervalTrigger(seconds=1))
        # 开始执行定时任务调度器
        logger.error("开始定时任务")
        scheduler.start()
        time.sleep(3)
        logger.error("暂停定时任务")
        my_job.pause()
        time.sleep(3)
        logger.error("恢复定时任务")
        my_job.resume()
        time.sleep(3)
    except (KeyboardInterrupt, SystemExit):
        logger.error("进程已结束运行")






# 2.通过修饰器添加的任务，可以使用pause_job()方法暂停任务，使用resume_job()方法恢复任务

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
        logger.error("暂停定时任务")
        scheduler.pause_job(job_id="my_task")
        time.sleep(3)
        logger.error("恢复定时任务")
        scheduler.resume_job(job_id="my_task")
        time.sleep(3)
    except (KeyboardInterrupt, SystemExit):
        logger.error("进程已结束运行")












