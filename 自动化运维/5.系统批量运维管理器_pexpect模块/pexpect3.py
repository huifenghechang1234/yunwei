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
常用FTP协议实现自动化、集中式的文件备份，要求做到账号登录、文件上传与下
载、退出等实现自动化操作，本示例使用pexpect 模块的spawnu0方法执行FTP命令，通过
expect0方法定义匹配的输出规则，sendline0)方法执行相关FTP交命令等
"""
import pexpect
import sys
child = pexpect.spawnu('ftp ftp.openbsd.org') #  运行ftp命令
child.expect('(?i)name *:') #  (?)表示后面的字符串正则匹配忽略大小写
child.sendline('anonymous')   # 输入ftp 账号信息
child.expect('(?i)password') # 匹配密码输入提示
child.sendline('pexpect@sourceforge.net') # 输入ftp 密码
child.expect('ftp')   # 启用二进制传输模式
child.sendline('bin')
child.expect('ftp>')
child.sendline('get robots.txt') #  下载robots.txt 文件
child.expect('ftp>')
sys.stdout.write(child.before) #  输出匹配“ftp>”之前的输入与输出
print("Escape character is ].\n")
sys.stdout.write(child.after)
sys.stdout.flush()

# 调用 interact() 让出控制权，用户可以继续当前的会话手工控制子程序，默认输入“~]”字符跳出
child.interact()
child.sendline('bye')
child.close()
