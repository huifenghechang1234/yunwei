import os
from myCeleryProj.app import app
import time
import socket


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
    s = x + y
    time.sleep(3)  # 模拟耗时操作
    print("主机IP {}: x + y = {}".format(get_host_ip(), s))
    return s


@app.task
def taskA():
    print("taskA begin...")
    print(f"主机IP {get_host_ip()}")
    time.sleep(3)
    print("taskA done.")


@app.task
def taskB():
    print("taskB begin...")
    print(f"主机IP {get_host_ip()}")
    time.sleep(3)
    print("taskB done.")
