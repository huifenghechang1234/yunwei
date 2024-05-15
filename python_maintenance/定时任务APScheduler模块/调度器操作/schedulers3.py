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
故障排查
如果 scheduler 没有如预期般正常运行，可以尝试将apscheduler的 logger 的日志级别提升到DEBUG等级
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
import logging

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)


# 定时任务执行函数
def my_task():
    logger.info("执行task任务")


if __name__ == '__main__':
    try:
        # 实例化调度器对象
        scheduler = BackgroundScheduler()
        # 添加定时任务，指定任务函数和触发器
        my_job = scheduler.add_job(my_task, trigger=IntervalTrigger(seconds=2))
        logger.error("开始定时任务")
        # 开始执行定时任务调度器
        scheduler.start()
        time.sleep(3)
    except (KeyboardInterrupt, SystemExit):
        logger.error("进程已结束运行")

