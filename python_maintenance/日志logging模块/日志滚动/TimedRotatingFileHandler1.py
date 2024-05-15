"""
title = ''
author = 'huifenghechang'
mtime = '2024/3/3'
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

日志滚动是一种常见的日志管理方式，它可以控制日志文件的大小或者按照一定时间间隔自动创建新的日志文件，
避免单个日志文件过大或日志文件数量过多

在Python的logging模块中，有两种常见的日志滚动方式：

按大小滚动：当日志文件达到一定大小时，自动创建新的日志文件，旧的日志文件重命名或压缩。
按时间滚动：每隔一定时间间隔，自动创建新的日志文件，旧的日志文件以日期或时间命名

TimedRotatingFileHandler()方法格式：
TimedRotatingFileHandler(filename="文件名”，when="时间周期单位”，interval=实践间隔,
backupCount=日志数量)
"""

import logging
from logging.handlers import TimedRotatingFileHandler
import time

# 创建一个Logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 创建一个TimedRotatingFileHandler
handler = TimedRotatingFileHandler('example1.log', when='midnight', interval=1, backupCount=5)
handler.setLevel(logging.INFO)

# 创建一个Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# 将Handler添加到Logger
logger.addHandler(handler)

# 记录日志消息
for i in range(10):
    logger.info('This is a test message %d' % i)
    time.sleep(1)
