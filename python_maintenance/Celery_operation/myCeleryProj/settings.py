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
配置信息
"""

BROKER_URL = 'redis://10.0.0.129:6379/0'  # 使用redis作为消息代理
CELERY_RESULT_BACKEND = 'redis://10.0.0.129:6379/0'   # 任务结果存在redis
CELERY_RESULT_SERIALIZER = 'json'
CELERY_RESULT_RESULT_EXPIRES = 60 * 60 * 24  # 任务过期时间
