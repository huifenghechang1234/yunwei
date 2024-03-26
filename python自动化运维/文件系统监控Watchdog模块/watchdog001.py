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
watchdog是一个Python模块，用于监视文件系统中文件的变化。它可以在文件被创建、修改、删除或重命名时触发相应的事件，
这使得你可以编写程序来响应这些变化

watchdog基本方法
"""

import time
from watchdog.observers import Observer  # 从watchdog.observers模块中导入Observer类，它用于监视文件系统的变化
from watchdog.events import FileSystemEventHandler  # 从watchdog.events模块中导入FileSystemEventHandler类，它是一个基类，用于处理文件系统事件


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f'File {event.src_path} has been modified')

    def on_created(self, event):
        if event.is_directory:
            return
        print(f'File {event.src_path} has been created')


if __name__ == "__main__":
    observer = Observer()  # 创建了一个观察者对象
    event_handler = MyHandler()  # 创建了一个自定义事件处理器对象
    observer.schedule(event_handler, path='.')  # 将自定义事件处理器注册到观察者对象中，并指定要监视的路径为当前目录
    observer.start()  # 启动观察者对象，开始监视文件系统的变化

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()  # 在捕获到Ctrl+C信号时，停止观察者对象

    observer.join()  # 等待观察者线程的结束
