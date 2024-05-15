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
celery执行延迟任务
"""

# 延迟任务，延迟5s钟后，发送短信
from user_task import send_sms
from datetime import datetime, timedelta
# print(datetime.utcnow()+timedelta(seconds=10))  # 打印出当前utc时间
eta=datetime.utcnow() + timedelta(seconds=10)  # 当前utc时间，往后推10s，时间对象
# # args是列表，send_sms的参数，eta是延迟时间，时间对象
res=send_sms.apply_async(args=['1888888',], eta=eta)
print(res)