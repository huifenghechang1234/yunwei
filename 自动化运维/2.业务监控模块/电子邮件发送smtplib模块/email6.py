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
群邮件
"""

import smtplib
from email.mime.text import MIMEText

sender = '***'
receiver = ['***', '****']
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = '***'
password = '***'

msg = MIMEText('你好', 'text', 'utf-8')

msg['Subject'] = subject

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
