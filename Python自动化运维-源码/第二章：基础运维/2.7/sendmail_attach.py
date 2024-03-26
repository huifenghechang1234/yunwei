# -*- coding: utf-8 -*-

import smtplib
import chardet
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header

# 第三方 SMTP 服务
mail_host = "mail.wjrcb.com"  # 设置服务器
mail_user = "zhengzheng"  # 用户名
mail_pass = "WQZZ2123"  # 口令


sender = "zhengzheng@wjrcb.com"
receivers = ["somenzz@qq.com", "somezz@163.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
message = MIMEMultipart()


message["From"] = sender  # 构造发件人，也可以使用Header构造
message["To"] = ";".join(receivers)  # 收件人列表，不是必须的
message["Subject"] = "这是主题：SMTP 邮件测试"

# 邮件正文内容



message.attach(MIMEText('<p>这是正文：图片及附件发送测试</p><p>图片演示：</p> <p><img src="cid:image1"></p>', 'html', 'utf-8'))

# 指定图片为当前目录
fp = open("1.jpg", "rb")
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header("Content-ID", "<image1>")
message.attach(msgImage)


#添加附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open("test.txt", "rb").read(), "base64", "utf-8")
att1["Content-Type"] = "application/octet-stream"
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)

# 添加附件2，传送当前目录下的 测试.txt 文件
att2 = MIMEText(open("测试.txt", "rb").read(), "base64", "utf-8")
att2["Content-Type"] = "application/octet-stream"
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att2.add_header("Content-Disposition", "attachment", filename=("gbk", "", "测试.txt"))
message.attach(att2)


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("发送成功")
except smtplib.SMTPException as e:
    print(f"发送失败,错误原因：{e}")
