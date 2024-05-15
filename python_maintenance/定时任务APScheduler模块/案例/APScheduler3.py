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
设置了一个后台调度器，并添加了一个每隔5秒执行一次的任务。这个任务尝试执行一个会
引发除以零异常的操作，并捕获异常以打印错误消息
"""
import logging
from apscheduler.schedulers.background import BackgroundScheduler

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 创建调度器
scheduler = BackgroundScheduler()


# 定义一个可能抛出异常的任务
def my_job():
    try:
        # 执行可能引发异常的代码
        result = 1 / 0
    except Exception as e:
        logging.error(f"任务执行出现异常: {str(e)}")

    # 添加任务到调度器，使用IntervalScheduler，每隔5秒执行一次


job_id = scheduler.add_job(my_job, 'interval', seconds=5, id='my_job_id')

# 启动调度器
scheduler.start()

# 阻塞当前进程，直到按下Ctrl+C
try:
    while True:
        pass
except (KeyboardInterrupt, SystemExit):
    # 关闭调度器
    scheduler.shutdown()
    logging.info("调度器已关闭")
