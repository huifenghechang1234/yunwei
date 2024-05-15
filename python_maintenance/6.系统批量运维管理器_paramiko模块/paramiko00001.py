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
paramiko模块方法
"""

# SSHClient常用的方法举例
import paramiko

# 实例化SSHClient
client = paramiko.SSHClient()
# 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接SSH服务端，以用户名和密码进行认证
client.connect(hostname='10.0.0.129', port=22, username='root', password='123456')
# 打开一个Channel并执行命令
stdin, stdout, stderr = client.exec_command('df -h ')  # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值
# 打印执行结果
print(stdout.read().decode('utf-8'))
# 关闭SSHClient
client.close()

# 密钥连接方式

# 配置私人密钥文件位置
private = paramiko.RSAKey.from_private_key_file('/Users/ch/.ssh/id_rsa')
# 实例化SSHClient
client = paramiko.SSHClient()
# 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接SSH服务端，以用户名和密码进行认证
client.connect(hostname='10.0.0.1', port=22, username='root', pkey=private)

# 创建一个通道
transport = paramiko.Transport(('hostname', 22))
transport.connect(username='root', password='123')
ssh = paramiko.SSHClient()
ssh._transport = transport
stdin, stdout, stderr = ssh.exec_command('df -h')
print(stdout.read().decode('utf-8'))
transport.close()

"""
SFTPClient常用方法介绍

SFTPCLient作为一个sftp的客户端对象，根据ssh传输协议的sftp会话，实现远程文件操作，如上传、下载、权限、状态
from_transport(cls, t)
创建一个已连通的SFTP客户端通道
put(localpath, remotepath, callback=None, confirm=True)
将本地文件上传到服务器
参数confirm：是否调用stat()
方法检查文件状态，返回ls - l的结果
get(remotepath, localpath, callback=None)
从服务器下载文件到本地
mkdir()
# 在服务器上创建目录
remove()
# 在服务器上删除目录
rename()
# 在服务器上重命名目录
stat()
# 查看服务器文件状态
listdir()
# 列出服务器目录下的文件
"""

# SFTPClient常用方法举例

# 获取Transport实例,初始化对象
tran = paramiko.Transport(('10.0.0.129', 22))

# 连接SSH服务端，使用password
tran.connect(username="root", password='123456')

# 或使用
# 配置私人密钥文件位置
private = paramiko.RSAKey.from_private_key_file('/Users/root/.ssh/id_rsa')

# 连接SSH服务端，使用pkey指定私钥
tran.connect(username="root", pkey=private)

# 获取SFTP实例，创建连接对象
sftp = paramiko.SFTPClient.from_transport(tran)

# 设置上传的本地/远程文件路径
localpath = "/Users/root/Downloads/1.txt"
remotepath = "/tmp/1.txt"

# 执行上传动作
sftp.put(localpath, remotepath)

# 执行下载动作
sftp.get(remotepath, localpath)

tran.close()
