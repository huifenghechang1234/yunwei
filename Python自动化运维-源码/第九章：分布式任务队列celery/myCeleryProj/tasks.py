import os
from myCeleryProj.app import app
import time


def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


@app.task
def add(x, y):
    time.sleep(3)  # 模拟耗时操作
    s = x + y
    print("主机IP {}: x + y = {}".format(get_host_ip(), s))
    return s


@app.task
def taskA():
    print("taskA")
    time.sleep(3)


@app.task
def taskB():
    print("taskA")
    time.sleep(3)
