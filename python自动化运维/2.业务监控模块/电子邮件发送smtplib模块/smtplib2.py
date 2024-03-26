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

操作步骤
	1.创建Smtp对象
	2.配置连接信息
	3.设定登录信息
	4.设定邮件内容信息
	5.断开连接
	
	校验码  HNSMCLMQJOSTSUEQ
"""

import smtplib
import string

"""
第一种方法
"""
# # 邮件内容定制
# HOST = "smtp.163.com"  # 定义smtp主机
# SUBJECT = "Test email from Python"  # 定义邮件主题
# TO = "2213024107@qq.com"  # 定义邮件收件人
# FROM = "17398485570@163.com"  # 定义邮件发件入
# text = "Python rules them all!"  # 邮件内容
# BODY = "\n".join((  # 组装 sendmail方法的邮件主体内容，各段以”rn”进行分隔
#     "From: %s" % FROM,
#     "To : %s" % TO,
#     "Subject:%s" % SUBJECT,
#     "",
#     text,
# ))
#
# # smtp的操作步骤
# server = smtplib.SMTP()  # 创建一个SMTP()对象
# server.connect(HOST, "25")  # 通过 connect 方法连接 smtp主机
# server.starttls()  # 启动安全传输模式
# server.login("17398485570@163.com", "HNSMCLMQJOSTSUEQ")  # 邮箱账号登录校验
# server.sendmail(FROM, [TO],BODY)  # 邮件发送
# server.quit()  # 断开smtp连接



"""
第二种方法
"""
HOST = "smtp.163.com"  # 定义smtp主机
POST = "25"
USER = "17398485570@163.com"
AUTH_PASSWD = "HNSMCLMQJOSTSUEQ"
RECEIVE_LIST = ["2213024107@qq.com"]  # 定义邮件收件人
FROM_LIST = ["17398485570@163.com"]  # 定义邮件发件入
SUBJECT = "python 邮件发送"
TEXT = "这是测试的内容，请求检查"
MESSAGE_CONNECT = "\n".join((
    "发送者：{},"
    "接受者信息：{},"
    "邮件主题：{},"
    "发送内容:{},"
).format(FROM_LIST, RECEIVE_LIST, SUBJECT, TEXT)).encode('utf-8')

server = smtplib.SMTP()  # 创建一个SMTP()对象
server.connect(HOST, POST)  # 通过 connect 方法连接 smtp主机
# server.starttls()  # 启动安全传输模式
server.login(USER, AUTH_PASSWD)  # 邮箱账号登录校验
server.sendmail(FROM_LIST, RECEIVE_LIST, MESSAGE_CONNECT)  # 邮件发送
server.quit()  # 断开smtp连接


