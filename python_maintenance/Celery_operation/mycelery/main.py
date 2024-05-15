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
主程序
"""

import os
from celery import Celery

# 创建celery实例对象
app = Celery("dbj")  # celery对象可以创建多个，所以我们最好给我们当前的celery应用起个名字，比如叫做dbj

# 把celery和django进行组合，需要识别和加载django的配置文件
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dbj.settings.dev')
# 如果只是使用了logging日志功能的话可以不写以下两句，因为logging是python提供的模块，但是将来可能使用celery来执行其他的django任务，所以我们先写上
import django

django.setup()

# 通过app对象加载配置
app.config_from_object("mycelery.config")

# 加载任务
# 参数必须必须是一个列表，里面的每一个任务都是任务的路径名称
# app.autodiscover_tasks(["任务1","任务2"])
app.autodiscover_tasks(["mycelery.sms", ])


