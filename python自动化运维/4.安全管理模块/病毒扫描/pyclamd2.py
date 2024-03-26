"""
title = ''
author = 'huifenghechang'
mtime = '2024/2/28'
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
import os

"""
单线程案例

代码思路：
1.扫描的业务逻辑
扫描模型、扫描信息

2.扫描主函数
参数确定、启动扫描、信息显示
"""
import pyclamd
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import logging.config
import logging


# 1.扫描的业务逻辑
class Scan(object):
    def __init__(self, ip, scan_type, scan_file):
        """
        扫描任务对象的基本信息
        """
        # 定制基本的任务对象属性
        self.ip = ip  # 扫描ip地址列表
        self.scan_file = scan_file  # 扫描文件路径
        self.scan_type = scan_type  # 扫描类型
        self.connstr = ''  # 漏洞库连接对象状态信息
        self.scan_result = ''  # 文件路径扫描的结果
        self.port = 3306  # 定制漏洞库的端口号


def run(self):
    """
    扫描的基本业务逻辑
    return:连接状态信息和扫描的结果
    """
    # 1.创建漏洞库的连接对象
    try:
        clamd_object = pyclamd.ClamdNetworkSocket(host=self.ip, port=self.port, timeout=2)
        # 判断连接对象是否建立成功
        if clamd_object.ping():  # 连接对象连接成功
            self.conn_str = self.ip + "连接成功，OK"

            # 2.根据扫描类型，使用对应方式扫描
            clamd_object.reload()  # 重载最新的病毒库
            if self.scan_type == "scan_file":  # 及时扫描
                message = clamd_object.scan_file(self.scan_file)
                self.scan_result = "及时扫描： {}\n".format(message)
            elif self.scan_type == "contscan_file":  # 批量扫描
                message = clamd_object.scan_file(self.scan_file)
                self.scan_result = "批量扫描： {}\n".format(message)

            time.sleep(1)
        else:  # 连接对象连接失败
            self.conn_str = self.ip + "连接失败，error"
            return

    except Exception as e:
        # 如果连接对象异常，则返回信息
        self.conn_str = self.ip + "连接异常，错误信息如下" + str(e)

    # 单线程返回普通的连接信息和扫描结果信息
    return self.conn_str, self.scan_result


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("文件被修改了 {}".format(event.src_path))
        file = event.src_path  # 一旦监控到文件被修改，就做出扫描操作
        if os.path.isfile(file):
            if '/.' not in file:
                ip_list = ['192.168.8.12', '192.168.8.12']  # 设定扫的ip
                scan_type = 'scan_file'  # 设定即时扫描的模式
                #  scan_type ='contscan_file' # 设定批量扫的模式
                # scan_type ='multiscan_file' # 设定批量扫的模式
                file_path = '/home/python/scripts'  # 要扫的文件路径
                # 注意:不要用我们的 /home/puthon/code 下面的子目录，容易出问题

    # 2.扫描主函数
    def scan_file(file_path, ip_list, scan_type):
        # 2.1 基本属性的定制
        ip_list = ip_list  # 接收扫描的ip地址
        scan_type = scan_type  # 接收扫描的类型
        file_path = file_path  # 接收扫描的文件路径

        # 2.2 扫描任务的执行
        for ip in ip_list:
            scan_obj = Scan(file_path, ip_list, scan_type)
            my_connstr, my_scanresult = scan_obj.run()

            # 2.3 信息的返回
            print("连接对象的状态信息:{}".format(my_connstr))
            print("文件路径的扫描结果:{}".format(my_scanresult))
            print("===============================")


if __name__ == '__main__':

    # 2.改造主函数执行
    file_path = '/home/data'  # 设定要扫描的文件路径
    event_handler = MyHandler()  # 使用我们定制的文件监控类
    observer = Observer()  # 创建监控对象
    observer.schedule(event_handler, path=file_path, recursive=True)
    observer.start()  # 以线程方式开启任务

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.start()
