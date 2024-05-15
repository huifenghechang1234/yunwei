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
使用sftp上传文件
"""

import paramiko

# 获取Transport实例
tran = paramiko.Transport("10.0.0.129", 22)
# 连接SSH服务端
tran.connect(username="root", password="westos")
# 获取SFTP实例
sftp = paramiko.SFTPClient.from_transport(tran)
# 设置上传的本地/远程文件路径
localpath = "passwd.html"  # 本地文件路径
remotepath = "/home/kiosk/Desktop/fish"  # 上传对象保存的文件路径
# 执行上传动作
sftp.put(localpath, remotepath)

tran.close()
