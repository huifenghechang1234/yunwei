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
实现了文件上传、下载、创建与删除
"""

import paramiko

# 设置SSH连接参数
username = "root"
password = "123456"
hostname = "10.0.0.129"
port = 22

try:

    # 尝试建立SSH连接并执行SFTP操作
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)

    # 创建SFTP客户端对象
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put("/home/user/info.db", "/data/user/info.db")  # 上传文件
    sftp.get("/data/user/infol.db", "/home/user/infoldb")  # 下载文件

    # 在远程服务器的/home/路径下创建一个名为userdir的目录，并设置其权限为0o0755（即只有所有者有读/写/执行权限，
    # 组用户有读/执行权限，其他用户有读/执行权限）
    # sftp.mkdir("/home/userdir", 0o0755)  # 创建目录

    sftp.rmdir("/home/userdir")  # 删除目录
    sftp.rename("/home/test.sh", "/home/testfile.sh")  # 文件重命名
    print(sftp.stat("/home/testfile.sh"))  # 打印文件信息
    print(sftp.listdir("/home"))  # 打印目录列表
    t.close()
except Exception as e:
    print(str(e))
