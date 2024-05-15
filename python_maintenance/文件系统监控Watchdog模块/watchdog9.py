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
设置一个定时器， 200毫秒后抓取快照，并与上一张快照比较。每当有事件发生时，检查定时器是否已经启动。
如果未启动，则直接启动定时器；否则，说明该事件距离上次事件不足200毫秒，可视为是同一组事件，此时终止定时器，再次重启
"""

import time
import os, threading
from watchdog.observers import Observer
from watchdog.events import *
from watchdog.utils.dirsnapshot import DirectorySnapshot, DirectorySnapshotDiff


class FileEventHandler(FileSystemEventHandler):
    def __init__(self, aim_path):
        FileSystemEventHandler.__init__(self)
        self.aim_path = aim_path
        self.timer = None
        self.snapshot = DirectorySnapshot(self.aim_path)

    def on_any_event(self, event):
        if self.timer:
            self.timer.cancel()

        self.timer = threading.Timer(0.2, self.checkSnapshot)
        self.timer.start()

    def checkSnapshot(self):
        snapshot = DirectorySnapshot(self.aim_path)
        diff = DirectorySnapshotDiff(self.snapshot, snapshot)
        self.snapshot = snapshot
        self.timer = None

        print("files_created:", diff.files_created)
        print("files_deleted:", diff.files_deleted)
        print("files_modified:", diff.files_modified)
        print("files_moved:", diff.files_moved)
        print("dirs_modified:", diff.dirs_modified)
        print("dirs_moved:", diff.dirs_moved)
        print("dirs_deleted:", diff.dirs_deleted)
        print("dirs_created:", diff.dirs_created)


#     def on_moved(self, event):
#         if event.is_directory:
#             print("directory moved from {0} to {1}".format(event.src_path,event.dest_path))
#         else:
#             print("file moved from {0} to {1}".format(event.src_path,event.dest_path))

#     def on_created(self, event):
#         if event.is_directory:
#             print("directory created:{0}".format(event.src_path))
#         else:
#             print("file created:{0}".format(event.src_path))

#     def on_deleted(self, event):
#         if event.is_directory:
#             print("directory deleted:{0}".format(event.src_path))
#         else:
#             print("file deleted:{0}".format(event.src_path))

#     def on_modified(self, event):
#         if event.is_directory:
#             print("directory modified:{0}".format(event.src_path))
#         else:
#             print("file modified:{0}".format(event.src_path))


class DirMonitor(object):
    """文件夹监视类"""

    def __init__(self, aim_path):
        """构造函数"""
        self.aim_path = aim_path
        self.observer = Observer()

    def start(self):
        """启动"""
        event_handler = FileEventHandler(self.aim_path)
        self.observer.schedule(event_handler, self.aim_path, True)
        self.observer.start()

    def stop(self):
        """停止"""
        self.observer.stop()


if __name__ == "__main__":
    monitor = DirMonitor(r"./monitor_folder_1")
    monitor.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        monitor.stop()
