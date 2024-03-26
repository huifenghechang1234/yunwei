"""
title = ''
author = 'huifenghechang'
mtime = '2024/3/17'
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
使用sftp下载文件
"""

import paramiko

# 获取SSHClient实例
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接SSH服务端
client.connect("10.0.0.129", username="root", password="123456")

# 获取Transport实例
tran = client.get_transport()

# 获取SFTP实例
sftp = paramiko.SFTPClient.from_transport(tran)

remotepath = '/home/kiosk/Desktop/fish'
localpath = '/home/kiosk/Desktop/fish'

sftp.get(remotepath, localpath)

client.close()
