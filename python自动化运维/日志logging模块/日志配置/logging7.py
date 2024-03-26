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
基于代码的配置
"""

import logging

# 创建一个Logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 创建一个FileHandler用于输出到文件
file_handler = logging.FileHandler('example2.log')
file_handler.setLevel(logging.INFO)

# 创建一个StreamHandler用于输出到控制台
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.ERROR)

# 创建一个Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# 设置Handler的Formatter
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# 将Handler添加到Logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# 记录日志消息
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
