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
使用RotatingFileHandler按照文件大小滚动的日志滚动
"""

import logging
from logging.handlers import RotatingFileHandler

# 创建一个Logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 创建一个RotatingFileHandler
# 创建了一个RotatingFileHandler，设置了日志文件的滚动方式为按照文件大小滚动（maxBytes=1024表示当日志文件大小达到1024字节时，
# 会创建一个新的日志文件），并指定了备份文件的数量为5个（backupCount=5），意味着最多保留5个旧的日志文件
handler = RotatingFileHandler('example2.log', maxBytes=1024, backupCount=5)
handler.setLevel(logging.INFO)

# 创建一个Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# 将Handler添加到Logger
logger.addHandler(handler)

# 记录日志消息
# 将这个处理器添加到Logger中，并记录了10条日志消息。在运行这个示例后，你会发现日志文件会在达到指定大小时自动滚动，
# 并保留指定数量的旧的日志文件
for i in range(10):
    logger.info('This is a test message %d' % i)

