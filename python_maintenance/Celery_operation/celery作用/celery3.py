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
celery执行定时任务


# 启动beat（beat负责定时提交任务）
celery beat -A celery_task -l info

# 启动worker，任务就会被worker执行了
celery -A celery_task worker -l info -P eventlet
"""

from datetime import timedelta
from celery.schedules import crontab

app.conf.beat_schedule = {
    # 定时任务一，每隔3秒做一次
    'task-mul': {
        'task': 'celery_task.user_task.mul',
        'schedule': timedelta(seconds=3),  # 3s后
        # 'schedule': crontab(hour=8, day_of_week=1),  # 每周一早八点
        'args': (3, 15),
    },
    # 定时任务二，每隔10秒做一次
    'task-add': {
        'task': 'celery_task.home_task.add',
        'schedule': timedelta(seconds=10),  # 10s后
        # 'schedule': crontab(hour=8, day_of_week=1),  # 每周一早八点
        'args': (3, 5),
    },
}

