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
监控文件夹中是否有后缀为".segy"的文件进入
"""

# 本模块的功能:<检测文件夹变化>

# 导入watchdog对应模块
from watchdog.observers import Observer
from watchdog.events import *
# 导入时间模块
import time


class FileEventHandler(FileSystemEventHandler):
    # 初始化魔术方法
    def __init__(self):
        FileSystemEventHandler.__init__(self)
        self.fileNameList = []  # 文件名列表（存储文件名）

    # 文件或文件夹移动
    def on_moved(self, event):
        if event.is_directory:
            print("directory moved from {0} to {1}".format(event.src_path, event.dest_path))
        else:
            print("file moved from {0} to {1}".format(event.src_path, event.dest_path))

    # 创建文件或文件夹
    def on_created(self, event):
        if event.is_directory:
            print("directory created:{0}".format(event.src_path))
        else:
            print("file created:{0}".format(event.src_path))
            fileAllName = str(event.src_path.split('/')[-1])
            if fileAllName.endswith('.segy'):
                self.fileNameList.append(fileAllName)
            print(self.fileNameList)

    # 删除文件或文件夹
    def on_deleted(self, event):
        if event.is_directory:
            print("directory deleted:{0}".format(event.src_path))
        else:
            print("file deleted:{0}".format(event.src_path))


#     # 修改文件或文件夹
#     def on_modified(self, event):
#         if event.is_directory:
#             print("directory modified:{0}".format(event.src_path))
#         else:
#             print("file modified:{0}".format(event.src_path))

if __name__ == "__main__":
    # 实例化Observer对象
    observer = Observer()
    event_handler = FileEventHandler()
    # 设置监听目录
    dis_dir = "./03_seis_data/"
    observer.schedule(event_handler, dis_dir, True)
    observer.start()
    try:
        while True:
            # 设置监听频率(间隔周期时间)
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

