"""
title = ''
author = 'huifenghechang'
mtime = '2024/1/6'
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
利用paramiko的invoke shell 机制来实现通过堡机实现服务器操作，原理
是SSHClient.connect 到堡垒机后开启一个新的 SSH会话(session)通过新的会话运行“sshuser@IP”去实现远程执行命令的操作。

用于通过Paramiko库连接到一个堡垒机（通常用于管理多个服务器的跳板机），然后尝试从堡垒机通过SSH登录到另一个业务服务器
"""

import paramiko
import os
import sys
import time

blip = "192.168.1.237"  # 定义堡垒机信息
bluser = "root"
blpasswd = "KJsdiuq45"
hostname = "192.168.1.21"

username = "root"  # 定义业务服务器信息
password = "IS8t5jgrie"
port = 22

passinfo = "'s password: "  # 输入服务器密码的前标志串
paramiko.util.log_to_file('syslogin3.log')  # 将paramiko操作过程中的信息留存下来

private = paramiko.RSAKey.from_private_key_file('/id_rsa')  # 加载秘钥文件

ssh = paramiko.SSHClient()  # 创建一个ssh客户端client对象

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 自动添加主机密钥
# 这意味着当连接到一个之前没有连接过的SSH服务器时，客户端会自动接受并添加服务器的SSH密钥到本地的 known_hosts 中

ssh.load_system_host_keys()  # 获取客户端host_keys,默认~/.ssh/known_hosts 非默认路径需指定
# 这行代码用于从系统的 known_hosts 文件中加载主机密钥。这通常是为了避免重复添加已知主机的密钥

try:
    ssh.connect(hostname=blip, username=bluser, password=blpasswd, pkey=private)  # 创建ssh连接
    channel = ssh.invoke_shell()  # 创建会话，开启命令调用
    channel.settimeout(10)  # 设置会话命令执行超时时间，单位为秒

    # 构建SSH登录业务主机的命令
    ssh_cmd = "ssh %s@%s" % (username, hostname)
    channel.send(ssh_cmd + "\n")  # 执行SSH登录业务主机，注意加上换行符

    buff = ''
    while True:
        if 'Are you sure you want to continue connecting' in buff:  # 检查是否出现SSH确认连接提示
            channel.send('yes\n')  # 如果是，则发送确认
            buff = ''  # 清空缓冲区
        if passinfo in buff:  # 检查是否出现密码提示
            channel.send(password + "\n")  # 如果是，则发送密码
            break  # 密码发送后跳出循环

        resp = channel.recv(9999).decode('utf-8')  # 接收响应并解码
        buff += resp  # 添加到缓冲区

        # 检查是否超时或SSH登录成功
        if "Permission denied" in buff or "Authentication failed" in buff:
            raise Exception("SSH login to the target server failed.")
        if "last login" in buff or "Welcome to" in buff:  # 检查是否登录成功
            print("SSH login to the target server succeeded.")
            break

except Exception as e:
    print('Error:', str(e))
finally:
    channel.close()  # 关闭会话
    ssh.close()  # 关闭SSH连接
