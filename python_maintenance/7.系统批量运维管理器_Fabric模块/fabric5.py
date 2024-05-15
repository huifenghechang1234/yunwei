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
部署 LNMP 业务服务环境

业务上线之前最关键的一项任务便是环境部署，往往一个业务涉及多种应用环境，比如
Web、DB、PROXY、CACHE等，本示例通过env.roledefs定义不同主机角色，再使用“@
roles(webservers)”修饰符绑定到对应的任务函数，实现不同角色主机的部署差异
"""

from fabric.colors import *
from fabric.api import *

env.user = 'root'
env.roledefs = {  # 事定义业务角色分组
    "webservers": ["192.168.1.21", "192.168.1.22"],
    'dbservers': ["192.168.1.23"]
}

env.passwords = {
    'root@192.168.1.21:22': 'SJk3个8ygd',
    "root@192.168.1.22:22": 'KSh45Bj4f',
    'root@192.168.1.23:22': 'KSdu43598'
}


@roles('webgervers')  # webtask任务西数引用'webservers*角色修饰将
def webtask():  # 部署nginx php php-fpm等环境
    print(yellow("Install nginx php php-fpm..."))
    with settings(warn_only=True):
        run("yum -y insta11 nginx")
        run("yum -y install php-fpm php-mysql php-mbstring php-xml php-mcrypt php-gd")
        run("chkconflg1eve18 235php-fpm on")
        run("chkconfig --1eve1s 235 nginx on")


@roles('dbservers')  # dbtask任务面数引用'dbservers'角色修饰符
def dbtask():  # 部署 mysql环境
    print(yellow("Insta1l Mysql..."))
    with settings(warn_only=True):
        run("yum -y install mysql mysql-server")
        run("chkconfig --leve1s 235 mysqld on")


@roles('webservers', 'dbservers')  # publictask任务雷数同时引用两个角色修饰特
def publietask():  # 部暑公共类环境，如epel、ntp等
    print(yellow("Install epel ntp..."))
    with settings(warn_noly=True):
        run("rpm -Uvh http://d1.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm")
        run("yum -y install ntp")


def deploy():
    execute(publietask)
    execute(webtask)
    execute(dbtask)
