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
使用线程和多进程执行 Watchdog 来启动独立进程
可以运行 Watchdog，使用线程和多进程并行处理多个文件
"""

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os
import ntpath
import time
import optparse
import multiprocessing
import threading
from collections import OrderedDict
import logger

lock = threading.RLock()


def process_function(get_event, event_dict):
    print(f"Process started for event: {get_event}")
    dir_path = ntpath.abspath(get_event)
    file_name = ntpath.basename(get_event)

    if len(get_event) > 0:
        pass

class Handler(PatternMatchingEventHandler):
    def __init__(self, queue):
        PatternMatchingEventHandler.__init__(self, patterns=['*.csv'],
                                             ignore_patterns=[],
                                             ignore_directories=True)
        self.queue = queue

    def on_created(self, event):
        # logger.info(f"Wait while the transfer of the file is finished before processing it")
        # file_size = -1
        # while file_size != os.path.getsize(event.src_path):
        #     file_size = os.path. getsize(event.src_path)
        #     time.sleep(1)

        file = None
        while file is None:
            try:
                file = open(event.src_path)
            except OSError:
                logger.info('Waiting for file transfer')
                time.sleep(5)
                continue

        self.queue.put(event.src_path)

    def on_modified(self, event):
        pass


def start_watchdog(watchdog_queue, dir_path):
    logger.info(f"Starting Watchdog Observer\n")
    event_handler = Handler(watchdog_queue)
    observer = Observer()
    observer.schedule(event_handler, dir_path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except Exception as error:
        observer.stop()
        logger.error(f"Error: {str(error)}")
    observer.join()


if __name__ == '__main__':
    dir_path = r'//file_path/'

    watchdog_queue = Queue()

    logger.info(f"Starting Worker Thread")
    worker = threading.Thread(target=start_watchdog, name="Watchdog",
                              args=(watchdog_queue, dir_path), daemon=True)
    worker.start()

    mp = Manager()
    event_dict = mp.dict()

    while True:
        if not watchdog_queue.empty():
            logger.info(f"Is Queue empty: {watchdog_queue.empty()}")
            pool = Pool()
            pool.apply_async(process_function, (watchdog_queue.get(), event_dict))
        else:
            time.sleep(1)
