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
date：某个特定时间仅运行一次 job
"""

import datetime
from apscheduler.schedulers.background import BackgroundScheduler


def job():
    print('job')


scheduler = BackgroundScheduler()
scheduler.start()

# 3 秒后运行
scheduler.add_job(
    job,
    trigger='date',
    run_date=datetime.datetime.now() + datetime.timedelta(seconds=3)
)

# 2019.11.22 00:00:00 运行
scheduler.add_job(
    job,
    trigger='date',
    run_date=datetime.date(2019, 11, 22),
)

# 2019.11.22 16:30:01 运行
scheduler.add_job(
    job,
    trigger='date',
    run_date=datetime.datetime(2019, 11, 22, 16, 30, 1),
)

# 2019.11.31 16:30:01 运行
scheduler.add_job(
    job,
    trigger='date',
    run_date='2019-11-31 16:30:01',
)

# 立即运行
scheduler.add_job(
    job,
    trigger='date'
)