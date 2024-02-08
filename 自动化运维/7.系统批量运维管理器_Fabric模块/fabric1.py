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
本示例调用local0方法执行本地(主控端)命令，添加“@runs once”修饰符保证该任
务函数只执行一次。调用run0方法执行远程命令
"""

from fabric.api import *

env.user='root'
env.hosts=['192.168.1.21','192.168.1.22']
env.password='LKs934jh3'

@runs_once #查看本地系统信息，当有多台主机时只运行一次
def local_task(): #本地任务函数
    local("uname-a")
def remote_task():
    with cd("/data/logs"):   #“with”的作用是让后面的表达式的语句继承当前状态，实现
        run("ls -I")  # “cd /data/logs && ls -l”的效果

