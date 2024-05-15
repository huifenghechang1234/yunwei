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

"""

import sys
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    # 设置日志信息格式
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    # 要监控的目录路径
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    # 创建一个日志事件处理程序
    event_handler = LoggingEventHandler()
    # 创建一个观察者对象
    observer = Observer()
    # 声明一个定时任务
    observer.schedule(event_handler, path, recursive=True)
    # 启动定时任务
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()

