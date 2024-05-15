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
批量远程密码连接
"""

import paramiko

from paramiko.ssh_exception import NoValidConnectionsError
from paramiko.ssh_exception import AuthenticationException


def connect(cmd, hostname, port, username, passwd):
    client = None
    try:
        client = paramiko.SSHClient()

        """
        这行代码设置了SSH客户端的缺失主机密钥策略。AutoAddPolicy()是一个策略，它告诉Paramiko在连接到一个之前未知的
        主机时自动接受并添加其SSH密钥到本地HostKeys对象。这通常用于自动化脚本，但请注意，在生产环境中，这可能会带来安全
        风险，因为恶意服务器可能会尝试中间人攻击。在生产环境中，更安全的做法是使用RejectPolicy或手动验证主机密钥
        """
        # client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        port = int(port)  # Convert port to integer
        client.connect(hostname=hostname, port=port, username=username, password=passwd)
        print(f'正在连接主机{hostname}......')

        # 这行代码在远程服务器上执行指定的命令（cmd变量）。exec_command方法返回三个文件对象：stdin（用于向命令发送输入），stdout（用于读取命令的标准输出），和stderr（用于读取命令的错误输出）
        stdin, stdout, stderr = client.exec_command(cmd)

        result = stdout.read().decode('utf-8')
        print(result)
    except NoValidConnectionsError as e:
        print(f"无法连接到主机 {hostname}: {str(e)}")
    except AuthenticationException as t:
        print(f"认证失败: {str(t)}")
    except ValueError as ve:
        print(f"无效的输入格式: {str(ve)}")
    except Exception as ex:
        print(f"发生未知错误: {str(ex)}")
    finally:
        if client is not None:
            client.close()


with open('ip.txt') as f:
    for line in f:
        line = line.strip()
        try:
            hostname, port, username, passwd = line.split(':')
            print(hostname.center(50, '*'))
            connect('uname', hostname, port, username, passwd)
        except ValueError:
            print("无效的输入格式，请确保每行包含主机名、端口、用户名和密码，并用冒号分隔。")
