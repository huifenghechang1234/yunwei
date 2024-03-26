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
paramiko的再封装
"""

import os
import paramiko
from paramiko.ssh_exception import NoValidConnectionsError, AuthenticationException, SSHException


class SshRemoteHost(object):
    def __init__(self, hostname, port, user, passwd, cmd):
        self.hostname = hostname
        self.port = port
        self.user = user
        self.passwd = passwd
        self.cmd = cmd

    def run(self):
        """默认调用的内容"""
        # cmd hostname
        # put
        # get
        cmd_str = self.cmd.split()[0]  # cmd
        # 类的反射，判断类里面是否可以支持该操作
        if hasattr(self, 'do_' + cmd_str):  # do_cmd
            getattr(self, 'do_' + cmd_str)()
        else:
            print("目前不支持该功能")

    def do_cmd(self):
        client = paramiko.SSHClient()

        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:

            client.connect(hostname=self.hostname,
                           port=self.port,
                           username=self.user,
                           password=self.passwd)

            print("正在连接%s......." % (self.hostname))
        except NoValidConnectionsError as e:
            print("连接失败")
        except AuthenticationException as e:
            print("密码错误")
        else:
            # 4. 执行操作
            cmd = ''.join(self.cmd.split()[1:])  ##将输入的后面的取出，作为
            stdin, stdout, stderr = client.exec_command(cmd)

            # 5.获取命令执行的结果
            result = stdout.read().decode('utf-8')
            print(result)
        finally:
            # 6.关闭连接
            client.close()

    def do_put(self):
        # put /tmp/passwd  ###将本地的/tmp/passwd上传到远端/tmp/passwd
        print('正在上传...')
        try:
            # 获取Transport实例
            tran = paramiko.Transport(self.hostname, int(self.port))  # 由于端口为整形，而我们用split方法得到的是str
            # 连接SSH服务端
            tran.connect(username=self.user, password=self.passwd)
        except SSHException as e:
            print('连接失败')
        else:
            # 获取SFTP实例
            sftp = paramiko.SFTPClient.from_transport(tran)
            newCmd = self.cmd.split()[1:]
            if len(newCmd) == 2:

                # 设置上传的本地/远程文件路径
                localpath = newCmd[0]
                remotepath = newCmd[1]
                # 执行上传动作
                sftp.put(localpath, remotepath)
                print('%s文件上传到%s主机的%s文件成功' % (localpath, self.hostname, remotepath))
            else:
                print('上传文件信息错误')

                tran.close()

    def do_get(self):

        print('正在下载...')
        try:
            # 获取Transport实例
            tran = paramiko.Transport(self.hostname, int(self.port))  # 由于端口为整形，而我们用split方法得到的是str
            # 连接SSH服务端
            tran.connect(username=self.user, password=self.passwd)
        except SSHException as e:
            print('连接失败')
        else:
            # 获取SFTP实例
            sftp = paramiko.SFTPClient.from_transport(tran)
            newCmd = self.cmd.split()[1:]
            if len(newCmd) == 2:

                # 设置下载的本地/远程文件路径
                localpath = newCmd[1]
                remotepath = newCmd[0]
                # 执行上传动作
                sftp.get(remotepath, localpath)
                print('%s主机的%s文件下载到%s文件成功' % (self.hostname, remotepath, localpath))
            else:
                print('上传文件信息错误')

                tran.close()


import paramiko
import os

# 1.选择操作的主机组:eg:mysql,web,ftp
groups = [file.rstrip('.conf') for file in os.listdir('conf')]
print("主机组显示：".center(50, '*'))
for group in groups:
    print('\t', group)
choiceGroup = input("选择批量操作的主机组(eg:mysql):")

# 2.根据选择的主机组，显示包含的主机IP/主机名
# 1).打开文件conf/choiceGroup.conf
# 2).依次读取文件每一行
# 3).只拿出
print("主机组包含的主机：".center(50, '*'))
with open('conf/%s.conf' % (choiceGroup)) as f:
    for line in f:
        print(line.split(':')[0])
    f.seek(0, 0)  ##把指针移动到文件最开始
    hostinfos = [line.strip() for line in f.readlines()]

# 3.让用户确认信息，选择需要批量执行的命令；
#     -cmd shell 命令
#     -put 本地文件  远程文件
#     -get 远程文件  本地文件
print("批量执行脚本".center(50, "*"))
while True:
    cmd = input('>>:').strip()
    if cmd:
        if cmd == 'exit' or cmd == "quit":
            print("执行完毕，正在退出")
            break
        for info in hostinfos:
            host, port, user, passwd = info.split(':')
            clientObj = SshRemoteHost(host, port, user, passwd, cmd)
            clientObj.run()
