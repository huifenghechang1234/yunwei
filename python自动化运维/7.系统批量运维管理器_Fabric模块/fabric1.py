"""
title = ''
author = 'huifenghechang'
mtime = '2024/1/5'
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
查看本地与远程主机信息
本示例调用local0方法执行本地(主控端)命令，添加“@runs_once”修饰符保证该任
务函数只执行一次。调用run()方法执行远程命令
"""

from fabric.api import *
from fabric.connection import Connection

# Set the connection parameters
user = 'root'
hosts = ['192.168.1.21', '192.168.1.22']
password = 'LKs934jh3'


# Decorator to ensure a task runs only once
def runs_once(func):
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, 'has_run'):
            wrapper.has_run = True
            return func(*args, **kwargs)

    return wrapper


# Define a task to run a command locally
@task
@runs_once
def local_task(c):
    c.local("uname -a")


# Define a task to run a command remotely
@task
def remote_task(c):
    with c.cd("/data/logs"):
        c.run("ls -l")


# Create a connection context manager
def connect(host):
    return Connection(host=host, user=user, connect_kwargs={"password": password})


# Main function to execute tasks on remote hosts
def main():
    for host in hosts:
        with connect(host) as conn:
            local_task(conn)  # Run local_task once for all hosts
            remote_task(conn)  # Run remote_task for each host


if __name__ == "__main__":
    main()

