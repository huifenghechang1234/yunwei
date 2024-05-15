"""
title = ''
author = 'huifenghechang'
mtime = '2024/4/22'
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
邮件群发器

这款自动化脚本可利用 Gmail 自带的 SMTP 服务器，在几分钟内批量发送电子邮件，让你可以完全自定义并行使权力
"""

import smtplib
import ssl

# SMTP server details
smtp_server = 'data.STUDIO.com'
smtp_port = 465

# Sender and recipient details
from_address = 'Winzo Shop'
to_address = ['','']     ## Recepients List

# Authentication details
username = ''       ## Sender Email
password = ''       ## Sender Password


# Email message details
subject = '🎉 Exclusive Offer Inside! Get 10% Off Your Next Purchase'
body = '''
亲爱的读者

🏴‍☠️宝藏级🏴‍☠️ 原创公众号『数据STUDIO』内容超级硬核。公众号以Python为核心语言，垂直于数据科学领域，包括可戳👉 Python｜MySQL｜数据分析｜数据可视化｜机器学习与数据挖掘｜爬虫 等，从入门到进阶！

欢迎关注

致以最诚挚的问候、
@公众号：数据STUDIO
'''

# Create an SSL/TLS context
context = ssl.create_default_context()

# Connect to the SMTP server using SSL/TLS
with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
    # Enable debugging to print the server's responses
    server.set_debuglevel(1)

    # Login to the SMTP server
    server.login(username, password)

    # Create the email message
    message = f'From: {from_address}\r\nSubject: {subject}\r\nTo: {to_address}\r\n\r\n{body}'
    message = message.encode()  # Convert the message to bytes

    # Send the email
    server.sendmail(from_address, to_address, message)