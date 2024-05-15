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
实现自动密钥登录方式，第一步需要配置与目标设备的密钥认证支持，具体见9.2.5节
私钥文件可以存放在默认路径“~/ssh/id rsa”，当然也可以自定义，如本例的“/home/keyl
id rsa”，通过paramiko.RSAKey.from_private key fle0方法引用
"""

import paramiko
import os

# 设置连接参数
hostname = '10.0.0.129'
username = 'root'
password = '123456'

# 开启日志
paramiko.util.log_to_file('syslogin.log')

# 创建 SSH 客户端对象
ssh = paramiko.SSHClient()

# 加载系统主机密钥
ssh.load_system_host_keys()  # 加载系统默认的主机密钥，用于验证服务器的身份。这有助于防止中间人攻击

# 定义私钥路径并创建私钥对象
# privatekey = os.path.expanduser('/home/key/id_rsa')  # 定义私销存放路径
# key = paramiko.RSAKey.from_private_key_file(privatekey)  # 创建私钥对象key

# 建立 SSH 连接
ssh.connect(hostname=hostname, username=username, password=password)

"""
通过 SSH 连接执行 free -m 命令（这个命令用于查看系统的内存使用情况）。exec_command 方法返回三个对象：stdin（用于向远程进程发送输入）、
stdout（用于读取远程进程的输出）和 stderr（用于读取远程进程的错误输出）。这里我们只关心 stdout，并打印其内容
"""
stdin, stdout, stderr = ssh.exec_command('free -m')
# stdin, stdout, stderr = ssh.exec_command('ls -lh /root')

# 执行远程命令
print(stdout.read())
ssh.close()
