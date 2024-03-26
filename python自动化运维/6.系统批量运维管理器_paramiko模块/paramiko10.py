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
基于密钥的上传和下载
"""

import paramiko

private_key = paramiko.RSAKey.from_private_key_file('id_rsa')

tran = paramiko.Transport('172.25.254.31', 22)
tran.connect(username='root', password='westos')

# 获取SFTP实例
sftp = paramiko.SFTPClient.from_transport(tran)

remotepath = '/home/kiosk/Desktop/fish8'
localpath = '/home/kiosk/Desktop/fish1'

"""
使用SFTP客户端对象sftp的put方法，将本地文件（localpath指定的文件）上传到远程服务器的指定路径（remotepath）
"""
# 上传文件到远程服务器
sftp.put(localpath, remotepath)

"""
使用SFTP客户端对象sftp的get方法，从远程服务器的指定路径（remotepath）下载文件到本地的指定路径（localpath）
"""
# 从远程服务器下载文件到本地:
sftp.get(remotepath, localpath)
