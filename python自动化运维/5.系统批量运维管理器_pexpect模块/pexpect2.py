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
下面使用 pxssh类实现一个 ssh 连接远程主机并执行命的示例。首先使用 login0方法
与远程主机建立连接，再通过sendline0方法发送执行的命令，prompt0方法等待命令执行结
束且出现系统提示符，最后使用logout0方法断开连接
# """
# import pxssh   # pexxh模块不支持windows系统
# import getpass
#
# try:
#     s = pxssh.pxssh()  # 创建 pxssh 对象s
#     hostname = raw_input('hostname:')
#     username = raw_input('username:')
#     password=getpass,getpass('please input password:)  #接收密码输入
#     s.login(hostname,username,password) #建立ssh连接#运行uptime命令
#     s.sendline('uptime')  #匹配系统提示符
#     s.prompt()  #打印出现系统提示符前的命令输出
#     print(s.before)
#     s.sendline('ls-1')
#     s.prompt()
#     print(s.before)
#     s.sendline('df')
#     s.prompt()
#     print(s.before)
#     s.logout()  # 断开ssh 连接
# except pxssh.ExceptionPxssh as e:
#     print("pxssh failed on login.")
#     print(str(e))