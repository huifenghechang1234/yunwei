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
添加任务
add_job()是以传参的形式指定对应的函数名这种方法是最常用的，推荐使用此方法。此方法会返回一个apscheduler.job.Job
实例，这样就可以在运行时，修改或删除任务。
scheduled_job() 是以装饰器的形式直接对我们要执行的函数进行修饰，这种方法最方便，但缺点就是运行时，不能修改任务

"""
# main.py
# 导入调度器，此处使用BlockingScheduler阻塞调度器
from apscheduler.schedulers.blocking import BlockingScheduler
# 导入触发器，此处使用IntervalTrigger特定时间间隔触发
from apscheduler.triggers.interval import IntervalTrigger
# 导入日志记录器
from loguru import logger

# 实例化调度器对象
scheduler = BlockingScheduler()


# 定时任务执行函数
@scheduler.scheduled_job(trigger="interval", args=(1,), seconds=3)
def my_task(number):
    logger.info("开始执行任务,传入的参数是%s" % number)


if __name__ == '__main__':
    try:
        # 开始执行定时任务调度器
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logger.error("进程已结束运行")


