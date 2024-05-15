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

"""

from apscheduler.schedulers.background import BackgroundScheduler
from datetime import date, datetime

# 创建定时任务的调度器对象
scheduler = BackgroundScheduler()


# 定义定时任务，接受一个参数
def my_job(p1):
    print(f"执行任务，参数为：{p1}")


# 添加一个定时任务，在指定日期执行一次
# 注意：需要导入date类
scheduler.add_job(my_job, 'date', run_date=date(2020, 12, 13), args=['text'])

# 添加一个定时任务，每隔两分钟执行一次
scheduler.add_job(my_job, 'interval', minutes=2, args=[10])

# 添加一个定时任务，在指定时间段内每隔两分钟执行一次
# 注意：start_date和end_date应该是datetime对象，且需要包含时间信息
start_time = datetime(2020, 12, 13, 14, 0, 1)
end_time = datetime(2020, 12, 13, 14, 0, 10)
scheduler.add_job(my_job, 'interval', minutes=2, start_date=start_time, end_date=end_time, args=['interval_text'])

# 添加一个定时任务，使用cron表达式，在指定月份和时间的组合执行
# 注意：这里使用了未定义的job_func，应该替换为已定义的函数，如my_job
# 而且cron表达式中的day和hour字段需要确保匹配期望的时间
# 例如，这里应该使用'mon-tue'来表示星期一和星期二，并且需要为每个小时分别添加一个任务
# 由于cron不支持直接指定多个小时，所以需要为每个小时分别添加job
for hour in range(0, 4):
    scheduler.add_job(my_job, 'cron', month='1-3,7-9', day='mon-tue', hour=hour, args=[f'cron_job_hour_{hour}'])

# 启动定时任务调度器工作
scheduler.start()

# 阻塞当前进程，直到按下Ctrl+C
try:
    while True:
        pass
except (KeyboardInterrupt, SystemExit):
    # 关闭定时任务调度器
    scheduler.shutdown()