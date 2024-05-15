"""
title = ''
author = 'huifenghechang'
mtime = '2024/1/7'
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
动态获取远程目录列表
本示例使用“@task”修饰符标志入口函数go)对外部可见，配合“@runs once”修饰
符接收用户输人，最后调用 worktask0任务函数实现远程命令执行

该示例实现了一个动态输人远程目录名称，再获取目录列表的功能，由于我们只要求输
人一次，再显示所有主机上该目录的列表信息，调用了一个子函数 input raw0 同时配置@
runsonce修饰符来达到此目的。
"""

from fabric.api import *

env.user = 'root'
env.hosts = ['10.0.0.7']
env.password = '123456'


@runs_once  # 主机遍历过程中，只有第一台触发此函数
def input_raw():
    return prompt("please input directory name;", default="/home")


def worktask(dirname):
    run("ls -l " + dirname)


@task  # 限定只有go函数对 fab命令可见
def go():
    getdirname = input_raw()
    worktask(getdirname)

if __name__ == "__main__":
    worktask('/root')