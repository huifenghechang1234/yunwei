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

hostname = '192.168.1.211'
username = 'root'
paramiko.util.log_to_file('syslogin.log')
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
privatekey = os.path.expanduser('/home/key/id rsa')  # 定义私销存放路径
key = paramiko.RSAKey.from_private_key_file(privatekey)  # 创建私钥对象key
ssh.connect(hostname=hostname, username=username, pkey=key)
stdin, stdout, stderr = ssh.exec_command('free -m')
print(stdout.read())
ssh.close()
