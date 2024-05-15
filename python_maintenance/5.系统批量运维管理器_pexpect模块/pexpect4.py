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
在 Linux系统集群运营当中，时常需要批量远程执行 Linux命令，并且双向同步文件的
操作。本示例通过使用 spawn 方法执行 ssh、scp 命令的思路来实现
"""

import pexpect
import sys

ip = "10.0.0.199"  # 定义目标主机
user = "root"  # 目标主机用户
passwd = "123456"  # 目标主机密码
target_file = "*/data/logs/nginx_access.log"  # 目标主机nginx日志文件
child = pexpect.spawn('/usr/bin/ssh', [user + '@' + ip])  # 运行ssh命今

# 输入、输出日志写入mylog.txt 文件
fout = open('mylog.txt', 'wb')
child.logfile = fout
child.expect('(?i)password')  # 匹配password 字符串，(?i)表示不区别大小写
child.sendline(passwd)
try:
    child.expect('#')
    child.sendline('tar -czf /data/nginx access.tar.gz' + target_file)  # 打包nginx  #日志文件
    child.expect('#')
    print(child.before)
    child.sendline('exit')
    fout.close()
except 'EOF':  # 定义 EOE 异常处理
    print("expect EOF")  # 定义TIMEOUT 异常处理
except 'TIMEOUT':
    print("expect TIMEOUT")

child = pexpect.spawn('/usr/bin/scp', [user + '@' + ip + ':/data/nginx_access.tar.gz', '/home'])  # 启动scp 远程贝命令，实现将打包好的nginx日复制至本地 /home目录
fout = open('mylog.txt', 'wa')
child.logfile = fout
try:
    child.expect('(?i)password')
    child.sendline(passwd)

    child.expect(pexpect.EOF)  # 匹配缓冲区EOE(结尾)，保证文件复制正常完成
except 'EOF':
    print("expect EOF")
except 'TIMEOUT':
    print("expect TIMEOUT")



