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
app所在文件，celery连接和配置相关文件
"""

# 有app的这个py文件，必须叫celery

from celery import Celery

backend = 'redis://127.0.0.1:6379/1'  # 结果存储
broker = 'redis://127.0.0.1:6379/2'  # 消息中间件
app = Celery('test', broker=broker, backend=backend, include=[
    'celery_task.home_task',
    'celery_task.order_task',
    'celery_task.user_task'
])

# 定制定时任务
# 时区(修改时区)
print(app.conf)
app.conf.timezone = 'Asia/Shanghai'
# 是否使用UTC
app.conf.enable_utc = False

# 任务的定时配置
from datetime import timedelta
from celery.schedules import crontab

app.conf.beat_schedule = {
    'send_sms_5': {
        'task': 'celery_task.user_task.send_sms',  # 要执行的任务
        'schedule': timedelta(seconds=5),
        # 'schedule': crontab(hour=8, day_of_week=1),  # 每周一早八点
        'args': (189533333,),
    },
    'add_3': {
        'task': 'celery_task.home_task.add',  # 要执行的任务
        'schedule': timedelta(seconds=3),
        # 'schedule': crontab(hour=8, day_of_week=1),  # 每周一早八点
        'args': (6, 8),
    }
}