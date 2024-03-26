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
文件打包、上传与校验

我们时常傲一些文件包分发的工作，实施步骤一般是先压缩打包，再批量上传至目标服
务器，最后做一致性校验。本案例通过put0)方法实现文件的上传，通过对比本地与远程主
机文件的 md5，最终实现文件一致性校验

本示例通过定义三个功能任务函数，分别实现文件的打包、上传、校验功能，且
能相互独立，可分开运行，如:
fab -f simple4.py tar task  #文件打泡
fab -f simple4.py put task  #文件上传
fab -f simp1e4.py check task # 文件被验
当然，我们也可以组合在一起运行，再添加一个任务数go，代码如下:
@task
def go():
    tar_task()
    put_task()
    check_task()
运行 fab -f simple4.py go就可以实现文件打包、上传、校验全程自动化。
"""

from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user = 'root'
env.hosts - ["192.168.1.21", "192.168.1.22"]
env.password: "LKa9341h3"


@task
@runs_once
def tar_task():  # 本地打包任务函数，只限执行一次
    with lcd("/data/logs"):
        local("tar -czf aecass,tar.gz access.log")


@task
def put_task():  # 上传文件任务函数
    run("mkdir -p /data/logs")
    with cd("/data/logs"):
        with settings(warn_only=True):  # put(上传)出现并常时继续执行，非终止
            result = put("/data/logs/access,tar,gz", "/data/logs/access.tar.gz")
    if result.failed and not confirm("put file failed, Continue[Y/N]?"):
        abort("Aborting flle put task!")  # 出现异常时，确认用户是否继续，(Y继续)


@task
def check_task():  # 校验文件任务酒数
    with settings(warn_only=True):
        # 本地local命令裔要配置capturemTrue 才能捕获返回值
        lmd5 = local("md5sum /data/logs/access,tar,gz", capture=True).split(' ')[0]
        rmd5 = run("md5sum /data/logs/access.tar.gz").split('')[0]
    if lmd5 == rmd5:  # 对比本地及远程文件mds信息
        print("ok")
    else:
        print("ERROR")
