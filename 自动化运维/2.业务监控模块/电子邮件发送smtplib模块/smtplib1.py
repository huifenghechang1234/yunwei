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
"""
email.mime理解成smtplib模块邮件内容主体的扩展，从原先默认只支持纯文本格式扩展到HTML，
同时支持附件、音频、图像等格式，smtplib只负责邮件的投递即可
"""

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# 发件人
from_name = "Hehuyi_In"
# 发件邮箱
from_addr = "xxxxx@qq.com"
# 发件邮箱授权码，注意不是QQ邮箱密码
from_pwd = "jjjjjjjjjj"
# 收件邮箱
to_addr = "yyyyyy@qq.com"

# 邮件标题
my_title = "Hehuyi Test"
# 邮件正文
my_msg = "Hello World"

# MIMEText三个主要参数
# 1. 邮件内容
# 2. MIME子类型，plain表示text类型
# 3. 邮件编码格式，使用"utf-8"避免乱码
msg = MIMEText(my_msg, 'plain', 'utf-8')
msg['From'] = formataddr([from_name, from_addr])
# 邮件的标题
msg['Subject'] = my_title

# SMTP服务器地址，QQ邮箱的SMTP地址是"smtp.qq.com"
smtp_srv = "smtp.qq.com"

try:
    # 不能直接使用smtplib.SMTP来实例化，第三方邮箱会认为它是不安全的而报错
    # 使用加密过的SMTP_SSL来实例化，它负责让服务器做出具体操作，它有两个参数
    # 第一个是服务器地址，但它是bytes格式，所以需要编码
    # 第二个参数是服务器的接受访问端口，SMTP_SSL协议默认端口是465
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)

    # 使用授权码登录QQ邮箱
    srv.login(from_addr, from_pwd)

    # 使用sendmail方法来发送邮件，它有三个参数
    # 第一个是发送地址
    # 第二个是接受地址，是list格式，可以同时发送给多个邮箱
    # 第三个是发送内容，作为字符串发送
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    print('发送成功')
except Exception as e:
    print('发送失败')
finally:
    # 无论发送成功还是失败都要退出你的QQ邮箱
    srv.quit()
