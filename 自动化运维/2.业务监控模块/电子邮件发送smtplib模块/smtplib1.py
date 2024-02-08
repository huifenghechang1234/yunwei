"""
title = ''
author = 'huifenghechang'
mtime = '2023/12/10'
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
SMTP类定义
smtplib.SMTP([host[,port[,local_hostname[,timeout]]]])

参数说明：
host: SMTP服务器主机。 你可以指定主机的ip地址或者域名如: runoob.com，这个是可选参数。
port: 如果你提供了host参数, 你需要指定SMTP服务使用的端口号，一般情况下SMTP端口号为25。
local_hostname: 如果SMTP在你的本机上，你只需要指定服务器地址为localhost即可
"""
import smtplib

# smtpObj = smtplib.SMTP([host[, port[, local_hostname]]] )
# # smtpObj = smtplib.SMTP_SSL( [host [, port [, local_hostname]]] )
#
#
# #################### 示例一
# smtp = smtplib.SMTP()
# smtp.connect([host[, port]])  # 连接远程smtp主机方法，host为远程主机地址，port为远程主机smtp端口，默认为25，也可以直接使用host:port形式来表示，例如：SMTP.connect("smtp.163.com","25")
# smtp.starttls()  # 开启安全传输模式
# smtp.login("test@arcvideo.com", "pwd")  # 邮箱账号登录校验
# smtp.sendmail(FROM, [TO], BODY)  # 电子邮件发送smtplib模块
# smtp.quit()  # 断开smtp连接
#
# #################### 示例二
# smtp = smtplib.SMTP([host[, port]])
# smtp.login("test@arcvideo.com", "pwd")  # 邮箱账号登录校验
# smtp.set_debuglevel(1)  # 打印出和SMTP服务器交互的所有信息。
# smtp.sendmail(FROM, [TO], BODY)  # 电子邮件发送smtplib模块
# smtp.quit()  # 断开smtp连接