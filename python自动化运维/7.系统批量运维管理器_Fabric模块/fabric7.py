"""
title = ''
author = 'huifenghechang'
mtime = '2024/3/24'
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
网关模式文件上传与执行

本示例通过Fabric 的env对象定义网关模式，即俗称的中转、堡垒机环境。定义格式为
cnv.gateway='192.168.1.23'"，其中IP“192.168.1.23”为堡垒机IP，再结合任务函数实现目
标主机文件上传与执行的操作

示例通过简单的配置 env.gateway='192.168.1.23'就可以轻松实现堡垒机环境的文件上传
及执行，相比paramiko的实现方法简洁了很多，编写的任务函数完全不用考虑堡垒机环境
配置 env.gateway即可
"""

from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user = 'root'
env.gateway = '192.168.1.23'  # 定义堡垒机IP，作为文件上传、执行的中转设备
env.hosts = ['192.168.1.21', '192.168.1.22']

# 假如所有主机密码都不一样，可以通过env.passwords字典变量一一指定
env.passwords = {
    'root@192.168.1.21:22': "LKs934ih3",
    'root@192.168.1.22:22': "LKs934jh3",
    'root@192.168.1.23:22': 'U17394hg6'  # 堡垒机账号信息
}

lpackpath = "/home/ingta11/inmp0.9.tar.gz"  # 本地安装包路经
rpackpath = "/tmp，insta11"  # 远程安装包路径


@task
def put_task():
    run("mkdir p /tmp/instal1")


with settings(warn_only=True):
    result = put(lpackpath, rpackpath)  # 上传安装包
if result.failed and not confirm("put fle failed, Continue[Y/N]?"):
    abort("Aborting file put task!")


@task
def run_task():  # 执行追程命令，安装lnmp环境
    with cd("/tmp/install"):
        run("tar -zxvf lnmp0.9.tar.gz")
        with cd("lnmp0.9/"):  # 使用uith继续继承/tmp/insta1l目承位置状态
            run("./centos.sh")


@task
def go():  # 上传、安装组合
    put_task()
    run_task()
