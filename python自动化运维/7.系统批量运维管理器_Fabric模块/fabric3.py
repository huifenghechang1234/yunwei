"""
title = ''
author = 'huifenghechang'
mtime = '2024/3/19'
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
fabric的典型使用方式就是，创建一个Python文件，该文件包含一到多个函数，然后使用
fab命令调用这些函数
"""

from fabric.api import run, sudo, env

env.hosts = ['10.0.0.11', '10.0.0.12']
env.port = 22
env.user = 'root'


def hostname():
    run('hostname')


def ls(path='.'):
    run('ls {0}'.format(path))


def tail(path='/etc/passwd', line=10):
    sudo('tail -n {0} {1}'.format(line, path))
