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
paramiko远程密码连接
"""

import paramiko

# 1.创建一个ssh对象
client = paramiko.SSHClient()

# 2.解决问题:如果之前没有，连接过的ip，会出现选择yes或者no的操作，
# 自动选择yes
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 3.连接服务器
client.connect(hostname='10.0.0.129',
               port=22,
               username='root',
               password='123456')

# 4.执行操作
stdin, stdout, stderr = client.exec_command('hostname')

# 5.获取命令执行的结果
result = stdout.read().decode('utf-8')
print(result)

# 6.关闭连接
client.close()
