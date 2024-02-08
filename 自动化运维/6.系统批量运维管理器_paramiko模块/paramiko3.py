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
是SSHClient.connect 到堡垒机后开启一个新的 SSH会话(session)通过新的会话运行“ssh
user@IP”去实现远程执行命令的操作。
"""

import paramiko
import os,sys,time

blip="192.168.1.237"  #定义堡垒机信息
bluser="root"
blpasswd="KJsdiuq45"
hostname="192.168.1.21"

username="root"  #定义业务服务器信息
password="IS8t5jgrie"
port=22

passinfo='\'s password: ' # 输入服务器密码的前标志串
paramiko.util.log_to_file('syslogin.log')
ssh=paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   #ssh 登录堡垒机
ssh.connect(hostname=blip,username=bluser,password=blpasswd)

channel=ssh.invoke_shel1()  #创建会话，开启命令调用
channel.settimeout(10)  #会话命令执行超时时间，单位为秒
buff = ''
resp = ''
channel.send('ssh i+username+'@'+hostname+rin') # 执行ssh 登录业务主机
while not buff.endswith(passinfo):  #ssh登录的提示信息判断，输出串尾含有"'s password:”时退出while循环
    try:
        resp = channel.recv(9999)
    except Exception as e:
        print('Error info;s connection time.' % (str(e)))
