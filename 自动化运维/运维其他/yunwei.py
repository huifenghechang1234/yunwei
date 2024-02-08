"""
title = ''
author = 'huifenghechang'
mtime = '2023/11/29'
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
#  1.连接远程服务器并执行命令
import paramiko

# 创建 SSH 客户端
ssh = paramiko.SSHClient()

# 设置为自动接受服务器的 hostkey
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接远程服务器
ssh.connect(hostname='remote.server.com', username='user', password='password')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('ls -l /tmp')



#  2.解析日志文件并提取有用信息
import regex

# 读取日志文件
with open('log.txt', 'r') as f:
    log = f.read()

# 使用正则表达式匹配错误信息
errors = regex.findall(r'ERROR:\s+(.*)', log)

# 打印出所有匹配到的错误信息
for error in errors:
    print(error)



#  3.监控系统状态并发送警报
import psutil
import smtplib

# 获取 CPU 使用率
cpu_percent = psutil.cpu_percent()

# 判断 CPU 使用率是否超过阈值
if cpu_percent > 80:
    # 建立 SMTP 连接
    server = smtplib.SMTP('smtp.example.com')
    server.login('user', 'password')

    # 构造邮件内容
    message = 'CPU 使用率超过 80%：当前使用率为 {}%'.format(cpu_percent)
    subject = '警报：高 CPU 使用率'

    # 发送邮件
    server.sendmail('alert@example.com', 'admin@example.com', subject, message)
    server.quit()



#  4.批量部署软件或更新系统
from fabric import task

@task
def update_system(c):
    c.run('apt-get update')


#  执行备份和恢复任务
import shutil

# 备份文件
shutil.copy('/path/to/file', '/path/to/backup/file')



#  5.如果要备份整个目录，可以使用 shutil 库的 copytree 函数。
import shutil

# 备份目录
shutil.copytree('/path/to/dir', '/path/to')

