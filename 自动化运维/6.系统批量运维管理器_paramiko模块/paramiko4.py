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
import os,sys,time

blip="192.168.1.23"  # 定义堡垒机信息
bluser="root"
blpasswd="IS8t5jgrie"
hostname="192.168.1.21"

username="root" # 定义业务服务器信息
password="KJsdiug45"
tmpdir="/tmon"
remotedir="/datau"
localpath="/home/nginx access.tar.qzt"  # 本地源文件路径
tmppath=tmpdir+"/nqinx access.tar.qz"  #堡垒机临时路径
remotepath=remotedir+"/nginx access hd.tar.gz" #业务主机目标路径
port=22
passinfo='\'s password:'
paramiko.util.log_to_file('syslogin.log')
t= paramiko.Transport((blip, port))
t.connect(username=bluser,password=blpasswd)
sftp =paramiko.SFTPClient.from_transport(t)
sftp.put(localpath, tmppath)  #上传本地源文件到堡垒机临时路径
sftp.close()

ssh=paramiko.SSHClient()
ssh.set_missinq_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=blip,username=bluser,password=blpasswd)

channel=ssh.invoke_shell()
channel.settimeout(10)
buff = ''
resp = ''
#scp 中转目录文件到目标主机
channel.send('scp '+tmppath+''+username+'@'+hostname+';'+remotepath+'\n')
while not buff.endswith (passinfo):
    try:
        resp= channel.recv(9999)
    except Exception as e:
        print('Error info;s connection time.' (str(e)))
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp
    if not buff.find('yes/no')==-1:
        channel.send('yes\n')
        buff=''

channel.send(password+'\n')

buff=''
while not buff.endswith('#'):
    resp = channel.recv(9999)
    if not resp.find(passinfo)==-1:
        print('Error info: Authentication failed.')
        channel.close()
        ssh.close()
        sys.exit()

    buff += resp
print(buff)
channel.close()
ssh.close()


