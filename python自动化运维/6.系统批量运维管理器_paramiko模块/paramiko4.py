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
使用sftp.put0方法上传文件至堡机临时目录，再通过 send0方法执行 scp
命令，将堡垒机临时目录下的文件复制到目标主机
"""

import paramiko
import os
import sys
import time

blip = "192.168.1.23"  # 定义堡垒机信息
bluser = "root"
blpasswd = "IS8t5jgrie"
hostname = "192.168.1.21"

username = "root"  # 定义业务服务器信息
password = "KJsdiug45"
tmpdir = "/tmon"
remotedir = "/datau"
localpath = "/home/nginx_access.tar.gz"  # 本地源文件路径，修正文件名
tmppath = os.path.join(tmpdir, "nginx_access.tar.gz")  # 堡垒机临时路径，修正文件名
remotepath = os.path.join(remotedir, "nginx_access_hd.tar.gz")  # 业务主机目标路径，修正文件名
port = 22

paramiko.util.log_to_file('syslogin4.log')

# 连接到堡垒机
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=blip, username=bluser, password=blpasswd)

try:
    # 上传本地文件到堡垒机
    sftp = ssh.open_sftp()
    sftp.put(localpath, tmppath)
    sftp.close()

    # 通过scp命令从堡垒机传输文件到业务服务器
    scp_cmd = f"scp {tmppath} {username}@{hostname}:{remotepath}"
    stdin, stdout, stderr = ssh.exec_command(scp_cmd)

    # 处理scp命令的输出
    buff = ''
    while True:
        if stdout.channel.recv_ready():
            buff += stdout.read(9999).decode('utf-8')
            if "100%" in buff:  # 假设输出中包含"100%"表示传输完成
                print("File transfer completed.")
                break
        if stderr.channel.recv_ready():
            err = stderr.read(9999).decode('utf-8')
            if "yes/no" in err:  # 如果是第一次连接，可能会有一个SSH确认
                stdin.write('yes\n')
                stdin.flush()
            elif "password" in err:  # 如果是密码提示
                stdin.write(password + '\n')
                stdin.flush()
            else:
                print(f"Error: {err}")
                break

except Exception as e:
    print(f'Error: {str(e)}')
finally:
    ssh.close()
