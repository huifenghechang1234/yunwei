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
日志配置
基于配置文件的配置


logging_config.ini文件
logging_config.ini是一个配置文件，可以包含日志记录器、处理器、过滤器和格式器等的配置信息

使用基于配置文件的配置可以更方便地管理日志配置，尤其是在需要配置多个Logger、Handler、Filter
和Formatter时。配置文件可以采用INI格式或者JSON格式。

这是一个简单的INI格式的配置文件，其中包含了一个Logger、一个TimedRotatingFileHandler和一个StreamHandler，以及一个Formatter的配置信息
"""

import logging
from logging.config import fileConfig

# 加载配置文件
fileConfig('logging_config.ini')

# 创建一个Logger
logger = logging.getLogger()

# 记录日志消息
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')


