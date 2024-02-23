"""
title = ''
author = 'huifenghechang'
mtime = '2024/2/21'
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
1.
smtp服务器地址: smtp.126.com
smtp服务器端口:465

2 对象创建
smtplib.SMTP_SSL()

3 连接配置
- 创建对象的时候，直接配置连接地址，没有之前的 connect 方法
smtplib.SMTP_SSL(HOST，PORT)
"""

import smtplib

HOST = "smtp.163.com"  # 定义smtp主机
POST = "465"
USER = "17398485570@163.com"
AUTH_PASSWD = "HNSMCLMQJOSTSUEQ"
RECEIVE_LIST = ["2213024107@qq.com"]  # 定义邮件收件人
FROM_LIST = ["17398485570@163.com"]  # 定义邮件发件入
SUBJECT = "python 邮件发送"
TEXT = "这是测试-TLS的内容，请求检查"
MESSAGE_CONNECT = "\n".join((
    "发送者：{},"
    "接受者信息：{},"
    "邮件主题：{},"
    "发送内容:{},"
).format(FROM_LIST, RECEIVE_LIST, SUBJECT, TEXT)).encode('utf-8')

server = smtplib.SMTP_SSL(HOST, POST)  # 创建一个SMTP()对象
server.login(USER, AUTH_PASSWD)  # 邮箱账号登录校验
server.sendmail(FROM_LIST, RECEIVE_LIST, MESSAGE_CONNECT)  # 邮件发送
server.quit()  # 断开smtp连接
