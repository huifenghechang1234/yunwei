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
获取任务列表
可以使用get_jobs方法来获得机器上可处理的作业调度列表。方法会返回一个Job实例的列表，如果你仅仅对特定
的 job store 中的 job 感兴趣，可以将 job store 的别名作为第二个参数。
也可以使用print_jobs()来格式化输出作业列表以及它们的触发器和下一次的运行时间

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
    logger.info("执行任务")


if __name__ == '__main__':
    try:
        # 实例化调度器对象
        scheduler = BackgroundScheduler()
        # 添加定时任务，指定任务函数和触发器
        my_job = scheduler.add_job(my_task, trigger=IntervalTrigger(seconds=1))
        # 开始执行定时任务调度器
        scheduler.start()
        scheduler.print_jobs()
        print(scheduler.get_jobs())
    except (KeyboardInterrupt, SystemExit):
        logger.error("进程已结束运行")

