"""
title = ''
author = 'huifenghechang'
mtime = '2024/3/2'
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
分别输出一条不同日志级别的日志记录

"""

import logging
import os
import time


def get_logger(loggername='mylogger'):
    # 使用一个名字为mylogger的logger
    logger = logging.getLogger(loggername)
    # 设置logger的level为DEBUG
    logger.setLevel(logging.DEBUG)
    # 创建一个输出日志到控制台的StreamHandler
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s]:[%(filename)s]:%(name)s:%(levelname)s: %(message)s')
    stream_handler.setFormatter(formatter)
    # 给logger添加上handler
    logdir = os.path.dirname(__file__)
    print(f'日志文件所在的文件夹{logdir}')

    # 把log输出到当前目录下交usk.log的文件
    filename = '%s/usk.log' % (logdir)
    print(f'日志文件路径及日志文件名{filename}')

    file_handler = logging.FileHandler(filename)
    file_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)  # 把日志打印到控制台
    logger.addHandler(file_handler)  # 把日志打印到文件

    return logger


# 举例查看log的形式
logger = get_logger('get_log')


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        # 打印log的级别和错误信息
        logger.warning(e)


if __name__ == '__main__':
    main()
