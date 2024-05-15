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
paramiko基于公钥密钥连接

注意：
在代码中，注释提到'id_rsa'为本地局域网密钥文件，这意味着'id_rsa'文件应该存在于运行此脚本的本地机器上，并且该文件应包含有效的RSA
私钥，用于SSH连接的身份验证。

该脚本会尝试连接到局域网'172.25.254.X'内的所有主机（从.1到.254），但是并没有处理可能存在的网络延迟或连接超时问题。在实际应用中，
可能需要为每次连接设置超时时间，以避免脚本因为等待无响应的主机而挂起。

如果某些主机没有运行SSH服务或防火墙阻止了SSH端口（默认为22），那么这些主机将无法连接成功
"""

import paramiko

from paramiko.ssh_exception import NoValidConnectionsError, AuthenticationException


def connect(cmd, hostname, port=22, user='root'):

    # 创建一个新的SSH客户端对象
    client = paramiko.SSHClient()

    #  从名为'id_rsa'的文件中读取RSA私钥。这个私钥文件用于SSH连接的身份验证
    private_key = paramiko.RSAKey.from_private_key_file('id_rsa')
    # id_rsa为本地局域网密钥文件

    # 设置当连接到未知主机时的策略为自动接受并添加其SSH密钥
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname,
                       port=port,
                       username=user,
                       pkey=private_key
                       )

        stdin, stdout, stderr = client.exec_command(cmd)
    except NoValidConnectionsError as e:
        print("连接失败")
    except AuthenticationException as e:
        print("密码错误")
    else:

        result = stdout.read().decode('utf-8')
        print(result)
    finally:

        client.close()


for count in range(254):  # 循环遍历0到253的整数（共254个），用于生成局域网内的主机地址
    host = '172.25.254.%s' % (count + 1)
    print(host.center(50, '*'))
    connect('uname', host)
