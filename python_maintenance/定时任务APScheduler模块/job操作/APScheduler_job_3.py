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
删除任务
当从 scheduler 中移除一个 job 时，它会从关联的 job store 中被移除，不再被执行。如果想从调度器移除一个任务，
那么你就要从相应的任务储存器中移除它，这样才算移除了。有两种方式
1.调用remove_job()，参数为：任务ID，任务储存器名称。通过修饰器添加的任务，使用此方法删除任务
2.在通过add_job()创建的任务实例上调用remove()方法
"""

# 调用remove_job()，参数为：任务ID，任务储存器名称。通过修饰器添加的任务，使用此方法删除任务

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
    logger.info("开始执行任务")


if __name__ == '__main__':
    try:
        # 开始执行定时任务调度器
        logger.error("开始定时任务")
        scheduler.start()
        time.sleep(3)
        logger.error("删除定时任务")
        scheduler.remove_job(job_id="my_task")
    except (KeyboardInterrupt, SystemExit):
        logger.error("进程已结束运行")







"""
在通过add_job()创建的任务实例上调用remove()方法
"""
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
    logger.info("开始执行任务")


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
        logger.error("删除定时任务")
        my_job.remove()
    except (KeyboardInterrupt, SystemExit):
        logger.error("进程已结束运行")

