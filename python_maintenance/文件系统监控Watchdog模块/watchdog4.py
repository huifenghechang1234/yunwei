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
监控目录变化
观察者（observer）可以设置指定目录及其所有子目录，在文件或目录创建、删除或修改时调用相应的方法
（on_created、on_deleted 或 on_modified），观察者以无限循环的方式运行，可以被键盘中断打断
"""

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class EventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            print("Directory created:", event.src_path)
        else:
            print("File created:", event.src_path)

    def on_deleted(self, event):
        if event.is_directory:
            print("Directory deleted:", event.src_path)
        else:
            print("File deleted:", event.src_path)

    def on_modified(self, event):
        if event.is_directory:
            print("Directory modified:", event.src_path)
        else:
            print("File modified:", event.src_path)

event_handler = EventHandler()
observer = Observer()
observer.schedule(event_handler, "/path/to/dir", recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
