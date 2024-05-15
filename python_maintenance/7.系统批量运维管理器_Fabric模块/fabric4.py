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
生产环境代码包发布管理
程序生产环境的发布是业务上线最后一个环节，要求具备源码打包、发布、切换、回
滚、版本管理等功能，本示例实现了这一整套流程功能，其中版本切换与回滚使用了Linux
下的软链接实现。详细源码如下
"""

from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
from fabric.contrib.console import confirm
import time

env.user = 'root'
env.hosts = ['192.168.1.21192.168.1.22']
env.password = 'LKs934ih3'

env.project_dev_source = '/data/dev/Lwebadmin/ '  # #开发机项目主目录
env.project_tar_source = '/data/dev/releases/'  # 开发机项目压缩包存储目录
env.projectpackname = 'release'  # 项目压缩包名前级，文件名为release.tar.gz
env.deploy_project_root = '/data/www/Lwebadmin/'  # 项目生产环境主目录
env.deploy_release_dir = 'releases'  # 项目发布目录，位于主目录下面
env.deploy_current_dir = 'current'  # 对外服务的当前版本软链接
env.deploy_version = time.strftime("号Y号md") + "v2"  # 版本阾慑号


@runs_once
# 获得用户输入的版本号，以便做版本回滚操作
def input_versionid():
    return prompt("please input project rollback version ID:", default="")


@task
@runs_once
# 打包本地项目主目录，并将压缩包存储到本地压缩包目录
def tar_source():
    print(yellow("Creating source package..."))

    with lcd(env.project_devsource):
        local("tar -czf $s,tar.gz." % (env.project_tar_source + env.project_pack_name))
    print(green("Creating source package success!"))


@task
def put_package():  # 上传任务函数
    print(yellow("Start put package..."))
    with settings(warn_only=True):
        with cd(env.deploy_project_rootnv.deploy_release_dir):
            run("mkdir %s" % (env.deploy_version))  # 创建版本目录

        env.deploy_full_path = env.deploy_project_root + env.deploy_release_dir + "/" + env.deploy_version

    with settings(warn_only=True):  # 上传项目压缩包至此目录
        result = put(env.project_tar_source + env.project_pack_name + ",tar.gz", env.deploy_full_path)
    if result.failed and not confirm("put fle failed, Continue[Y/N]?"):
        abort("Aborting file put task!")

    with cd(env.deploy_full_path):  # 成功解压后删除压缩包
        run("tar -zxvf %s.tar.gz" % (env.project_pack_name))
        run("rm -rf %s.tar.gz" % (env.project_pack_name))
    print(green("Put & untar package success!"))


@task
def make_symlink():  # 为当前版本目录做软链接
    print(yellow("update current symlink"))
    env.deploy_full_path = env.deploy_project_root + env.deploy_release_dir + "/" + env.deploy_version


with settings(warn_only=True):  # 删除软链接，重新创建并指定软链源目录，新版本生效
    run("rm -rf %s" % (env.deploy_project_root + env.deploy_current_dir))
    run("1n -s %s %s" % (env.deploy_full_path, env.deploy_project_root + env.deploy_current_dir))
    print(green("make symlink suecess!"))


@task
def rollback():  # 顾本回滚任务函数
    print(yellow("rollback project version"))
    versionid = input_versionid()  # 获得用户输入的回滚版本号

    if versionid == '':
        abort("proiect version ID error,abort!")
    env.deploy_full_path = env.deploy_project_root + env.deploy_release_dir + "/" + versionid


run("rm -f $s" % env.deploy_project_root + env.deploy_current_dir)
run("1n -s %s %s" % (
env.deploy_full_path, env.deploy_project_root + env.deploy_current_dir))  # 删除软链接，重新创建并指定软链源目录，新版本生效
print(green("rollback success!"))


@task
def go():  # 自动化程序版本发布入口函数
    tar_source()
    put_package()
    make_symlink()

# from fabric.api import *
# from fabric.colors import yellow, green
# import time
#
# env.user = 'root'
# env.hosts = ['192.168.1.21', '192.168.1.22']
# env.password = 'LKs934ih3'
#
# env.project_dev_source = '/data/dev/Lwebadmin/'  # 开发机项目主目录
# env.project_tar_source = '/data/dev/releases/'  # 开发机项目压缩包存储目录
# env.project_pack_name = 'release'  # 项目压缩包名前缀，文件名为release.tar.gz
# env.deploy_project_root = '/data/www/Lwebadmin/'  # 项目生产环境主目录
# env.deploy_release_dir = 'releases'  # 项目发布目录，位于主目录下面
# env.deploy_current_dir = 'current'  # 对外服务的当前版本软链接
# env.deploy_version = time.strftime("%Y%m%d") + 'v2'  # 版本号格式化
#
# @runs_once
# def input_version_id():
#     return prompt("Please input project rollback version ID:", default="")
#
# @task
# @runs_once
# def tar_source():
#     print(yellow("Creating source package..."))
#     with lcd(env.project_dev_source):
#         local("tar -czf {}.tar.gz .".format(env.project_tar_source + env.project_pack_name))
#     print(green("Creating source package success!"))
#
# @task
# def put_package():
#     print(yellow("Start put package..."))
#     with settings(warn_only=True):
#         with cd(env.deploy_project_root + env.deploy_release_dir):
#             run("mkdir -p {}".format(env.deploy_version))  # 创建版本目录
#
#     with cd(env.deploy_project_root + env.deploy_release_dir + '/' + env.deploy_version):
#         result = put(env.project_tar_source + env.project_pack_name + ".tar.gz", '.')
#
#         if result.failed and not confirm("File upload failed. Continue anyway?"):
#             abort("Aborting file put task!")
#
#         run("tar -zxvf {}.tar.gz && rm -rf {}.tar.gz".format(env.project_pack_name, env.project_pack_name))
#         print(green("Put & untar package success!"))
#
# @task
# def make_symlink():
#     print(yellow("Update current symlink"))
#     env.deploy_full_path = env.deploy_project_root + env.deploy_release_dir + '/' + env.deploy_version
#
#     with settings(warn_only=True):
#         run("rm -rf {} && ln -s {} {}".format(
#             env.deploy_project_root + env.deploy_current_dir,
#             env.deploy_full_path,
#             env.deploy_project_root + env.deploy_current_dir
#         ))
#         print(green("Make symlink success!"))
#
# @task
# def rollback():
#     print(yellow("Rollback project version"))
#     version_id = input_version_id()
#
#     if version_id == '':
#         abort("Project version ID error, abort!")
#
#     env.deploy_full_path = env.deploy_project_root + env.deploy_release_dir + '/' + version_id
#
#     with settings(warn_only=True):
#         run("rm -f {} && ln -s {} {}".format(
#             env.deploy_project_root + env.deploy_current_dir,
#             env.deploy_full_path,
#             env.deploy_project_root + env.deploy_current_dir
#         ))
#         print(green("Rollback success!"))
#
# @task
# def go():
#     tar_source()
#     put_package()
#     make_symlink()
