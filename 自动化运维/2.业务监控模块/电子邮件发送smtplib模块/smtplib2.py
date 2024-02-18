"""
title = ''
author = 'huifenghechang'
mtime = '2023/12/27'
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
import code

"""
通过 Python 的smtplib 模块来实现邮件的发送功能 ， 模拟一个 smtp 客户端， 
通过与 smtp 服务器交互来实现邮件发送的功能 ， 这可以理解成 Foxmail 的发邮件功能
"""

import smtplib

HOST = "smtp.gmail.com"  # 定义smtp主机
SUBJECT = "Test email from Python"  # 定义邮件主题
TO = "2213024107@qq.com"  # 定义邮件收件人
FROM = "2213024107hyr@gmail.com"  # 定义邮件发件入
text = "Python rules them all!"  # 邮件内容
BODY = "\r\n".join((    # 组装 sendmail方法的邮件主体内容，各段以”rn”进行分隔
        "From: %s" % FROM,
        "To : %s" % TO,
        "Subject:%s" % SUBJECT,
        "",
        text,
        ))

server = smtplib.SMTP()  # 创建一个SMTP()对象

server.connect(HOST, "25")  # 通过 connect 方法连接 smtp主机
server.starttls()  # 启动安全传输模式
server.login("2213024107hyr@gmail.com", "HYR19971018")  # 邮箱账号登录校验
server.sendmail(FROM, [TO]. BODY)  # 邮件发送
server.quit()   # 断开smtp连接



