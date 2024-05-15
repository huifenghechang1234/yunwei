"""
title = ''
author = 'huifenghechang'
mtime = '2024/1/5'
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
实现远程 SSH 登录， 登录成功后显示／home 目录文件清单， 并通过日志文件记录所有的输入与输出
"""

import pexpect
import sys

child = pexpect.spawn('ssh root@10.0.0.199')
fout = open('mylog.txt', 'w')
child.logfile = fout

child.expect("passwd:")
child.sendline("dddd")
child.expect('#')
child.sendline('ls /home')
child.expect('#')
