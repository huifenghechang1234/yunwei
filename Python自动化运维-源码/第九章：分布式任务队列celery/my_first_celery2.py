#encoding=utf-8

from celery import Celery
import time
import socket

app = Celery('tasks', broker='redis://127.0.0.1:6379/0',backend ='redis://127.0.0.1:6379/0' )

def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


@app.task
def add(x, y):
    time.sleep(3) # 模拟耗时操作
    s = x + y
    print("主机IP {}: x + y = {}".format(get_host_ip(),s))
    return s

if __name__ == '__main__':
    app.start()

