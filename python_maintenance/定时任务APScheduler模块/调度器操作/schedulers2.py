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
调度器事件监听
可以为 scheduler 绑定事件监听器（event listen）。Scheduler 事件在某些情况下会被触发，而且它可能携带有关特
定事件的细节信息。为add_listener()函数提供适当的掩码参数（mask argument）或者是将不同的常数组合到一起，可以
监听特定类型的事件。可调用的listener可以通过event object作为参数而被调用

"""

# main.py
# 导入调度器，此处使用BackgroundScheduler阻塞调度器
from apscheduler.schedulers.background import BackgroundScheduler
# 导入触发器，此处使用IntervalTrigger特定时间间隔触发
from apscheduler.triggers.interval import IntervalTrigger
# 导入事件类
from apscheduler.events import EVENT_ALL
# 导入日志记录器
from loguru import logger
import time


# 定时任务执行函数
def my_task():
    logger.info("执行task任务")


# 事件监听函数
def my_listener(event):
    match event.code:
        case 4096:
            logger.info("任务被成功执行")
        case 32768:
            logger.info("任务已经提交到执行器中执行")
        case _:
            logger.info(event.code)


if __name__ == '__main__':
    try:
        # 实例化调度器对象
        scheduler = BackgroundScheduler()
        # 添加定时任务，指定任务函数和触发器
        my_job = scheduler.add_job(my_task, trigger=IntervalTrigger(seconds=2))
        logger.error("开始定时任务")
        # 开始执行定时任务调度器
        scheduler.start()
        scheduler.add_listener(my_listener, mask=EVENT_ALL)
        time.sleep(4)
    except (KeyboardInterrupt, SystemExit):
        logger.error("进程已结束运行")

