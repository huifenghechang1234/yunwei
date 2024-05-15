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
在 Watchdog 中进行日志记录
要记录事件，可以创建一个继承自 FileSystemEventHandler 类的自定义事件处理程序类，并重写与要记录的事件相对应的方法
"""

import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class LogEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            logging.info(f"File created: {event.src_path}")

    def on_modified(self, event):
        if not event.is_directory:
            logging.info(f"File modified: {event.src_path}")

logging.basicConfig(filename='watchdog.log', level=logging.INFO, format='%(asctime)s - %(message)s')
event_handler = LogEventHandler()
observer = Observer()
observer.schedule(event_handler, "/path/to/", recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

