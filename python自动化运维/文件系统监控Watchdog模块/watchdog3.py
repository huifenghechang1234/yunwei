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
使用 Celery 来启动/停止 Watchdog
"""

from celery import Celery
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os
import time

app = Celery('celery_ex.celery_apptask_ex', broker='redis://localhost:6379/0')


@app.task
def process_file(file_path):
    # do something with the file
    with open(file_path, 'r') as f:
        print(f.read())


class MyHandler(PatternMatchingEventHandler):
    def on_created(self, event):
        file_size = -1
        while file_size != os.path.getsize(event.src_path):
            file_size = os.path.getsize(event.src_path)
            print(file_size)
            time.sleep(1)

        if event:
            print("file created:{}".format(event.src_path))
            # call function here
            process_file.apply_async(args=(event.src_path,))


if __name__ == "__main__":
    observer = Observer()
    event_handler = MyHandler(patterns=["*.csv", "*.pdf"],
                              ignore_patterns=[],
                              ignore_directories=True
                              )
    observer.schedule(event_handler, path='./input_files', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

