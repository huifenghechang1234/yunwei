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
本示例调用local()方法执行本地(主控端)命令，添加“@runs_once”修饰符保证该任
务函数只执行一次。调用run()方法执行远程命令

Fabric 1 使用 @task 装饰器以及 fabric.api 中的函数来定义和执行远程任务，而 Fabric 2 使用
 Connection 类来创建与远程主机的连接，并通过该连接对象的方法执行命令。

如果您想使用 Fabric 2，您应该只使用 fabric.connection.Connection，并且不应该导入
 fabric.api。如果您想使用 Fabric 1，您应该只使用 fabric.api 中的函数，并且不应该使用 
 fabric.connection.Connection
"""

# from fabric.api import *
# from fabric.connection import Connection
#
# # Set the connection parameters
# user = 'root'
# hosts = ['10.0.0.7']
# password = '123456'
#
#
# # Decorator to ensure a task runs only once
# def runs_once(func):
#     def wrapper(*args, **kwargs):
#         if not hasattr(wrapper, 'has_run'):
#             wrapper.has_run = True
#             return func(*args, **kwargs)
#
#     return wrapper
#
#
# # Define a task to run a command locally
# @task
# @runs_once
# def local_task(c):
#     c.local("uname -a")
#
#
# # Define a task to run a command remotely
# @task
# def remote_task(c):
#     with c.cd("/root"):
#         c.run("ls -l")
#
#
# # Create a connection context manager
# def connect(host):
#     return Connection(host=host, user=user, connect_kwargs={"password": password})
#
#
# # Main function to execute tasks on remote hosts
# def main():
#     for host in hosts:
#         with connect(host) as conn:
#             local_task(conn)  # Run local_task once for all hosts
#             remote_task(conn)  # Run remote_task for each host
#
#
# if __name__ == "__main__":
#     main()




from fabric import Connection
import subprocess

# Set the connection parameters
user = 'root'
hosts = ['10.0.0.7']
password = '123456'


# Define a task to run a command locally
def local_task():
    # Fabric 2 does not have a built-in way to run local commands
    # You can use the subprocess module instead
    subprocess.run(["uname", "-a"], check=True)


# Define a task to run a command remotely
def remote_task(c):
    with c.cd("/root"):
        c.run("ls -l")

    # Create a connection context manager


def connect(host):
    return Connection(host=host, user=user, connect_kwargs={"password": password})


# Main function to execute tasks on remote hosts
def main():
    # 执行本地任务
    local_task()

    # 对每个主机执行远程任务
    for host in hosts:
        with connect(host) as conn:
            remote_task(conn)

    # for host in hosts:
    #     with connect(host) as conn:
    #         local_task()  # Fabric 2 does not provide a way to run local tasks through connections
    #         remote_task(conn)  # Run remote_task for each host


if __name__ == "__main__":
    main()