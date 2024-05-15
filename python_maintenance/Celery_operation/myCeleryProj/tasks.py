"""
title = ''
author = 'huifenghechang'
mtime = '2024/4/15'
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
在终端输入：celery -A myCeleryProj.app worker -c 3 -I info或者
celery -A myCeleryProj.app worker -c 3 --loglevel=info，执行
"""
import os
from python_maintenance.Celery_operation.myCeleryProj.app import app
import time
import socket


def get_host_ip():
    """
    查询本机的ip地址
    :return: ip
    """
    s = None
    try:
        # 使用socket模块创建了一个IPv4的UDP套接字
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # 连接到百度公共DNS服务器
        s.connect(("180.76.76.76", 80))

        # 使用getsockname方法获取套接字绑定的本地地址，并取该地址的IP部分（即[0]）
        ip = s.getsockname()[0]
    except Exception as e:
        print(f"Error getting IP address: {e}")
        ip = None
    finally:
        if s is not None:
            s.close()
    return ip

"""
get_host_ip 函数：
该函数通过创建一个UDP套接字并尝试连接到Google的公共DNS服务器（8.8.8.8）来获取本机的IP地址。
s.getsockname()[0] 返回套接字的本地地址，即本机的IP地址。
使用try-finally块确保无论是否发生异常，套接字都会被关闭
"""
@app.task
def add(x, y):
    time.sleep(9)
    s = x + y
    ip = get_host_ip()
    print(f"主机IP {ip}: x + y = {s}")  # 考虑在生产环境中使用日志记录而不是直接打印
    return s

"""
Celery任务：
add 任务：接受两个参数x和y，模拟耗时操作（time.sleep(3)），然后计算它们的和，并打印出包含本机IP地址和计算
结果的字符串。
taskA 和 taskB 任务：这两个任务都简单地模拟耗时操作（time.sleep(3)），并打印出任务名称
"""
@app.task()
def taskA():
    time.sleep(9)
    print("taskA")


@app.task()
def taskB():
    time.sleep(9)
    print("taskB")
