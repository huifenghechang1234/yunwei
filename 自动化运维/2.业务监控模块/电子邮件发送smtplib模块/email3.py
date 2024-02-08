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
发送图文格式邮件
当要求包含图片数据的邮件内容时，需要引用MIMEImage类，若邮件主体由多个MIME对象组成，
则同时需引用MIMEMultipart类来进行组装。

本示例通过MIMEText与MIMEImage类的组合来实现图文格式邮件的定制
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import formataddr

# 发件人
from_name = "Hehuyi_In"
# 发件邮箱
from_addr = "xxxx@qq.com"
# 发件邮箱授权码，注意不是QQ邮箱密码
from_pwd = "xxxxx"
# 收件邮箱
to_addr = "xxxx@qq.com"
# 邮件标题
my_title = "HTML+Image Test"


# 添加图片函数，参数1：图片路径，参数2：图片id
def addimg(src, imgid):
    fp = open(src, 'rb')  # 打开文件
    msg_image = MIMEImage(fp.read())  # 创建MIMEImage对象，读取图片内容并作为参数
    fp.close()  # 关闭文件
    msg_image.add_header('Content-ID', imgid)  # 指定图片文件的Content-ID,<img>标签src用到
    return msg_image


# 创建MIMEMultipart对象，采用related定义内嵌资源的邮件体
msg_multipart = MIMEMultipart('related')

# 创建MIMEText对象，HTML元素包括表格<table>及图片<img>
msg_text = MIMEText("""
<table width="600" border="0" cellspacing="0" cellpadding="4">
      <tr bgcolor="#CECFAD" height="20" style="font-size:14px">
        <td colspan=2>*SqlServer001 <a href="monitor.domain.com">更多>></a></td>
      </tr>
      <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
        <td>
         <img src="cid:001"></td><td> 
         <img src="cid:002"></td>
      </tr>
      <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
        <td>
        <img src="cid:003"></td><td>
        <img src="cid:004"></td>
      </tr>
</table>""", "html", "utf-8")  # <img>标签的src属性是通过Content-ID来引用的

# MIMEMultipart对象附加MIMEText及MIMEImage的内容
msg_multipart.attach(msg_text)
msg_multipart.attach(addimg("img/001.png", "001"))  # 图片路径与标签，001对应上方html中的<img src="cid:001">
msg_multipart.attach(addimg("img/002.png", "002"))
msg_multipart.attach(addimg("img/003.png", "003"))
msg_multipart.attach(addimg("img/004.png", "004"))

# 发件人
msg_multipart['From'] = formataddr([from_name, from_addr])
# 邮件标题
msg_multipart['Subject'] = my_title

# SMTP服务器地址
smtp_srv = "smtp.qq.com"

try:

    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)

    # 使用授权码登录QQ邮箱
    srv.login(from_addr, from_pwd)

    # 使用sendmail方法来发送邮件
    srv.sendmail(from_addr, [to_addr], msg_multipart.as_string())
    print('发送成功')
except Exception as e:
    print('发送失败')
finally:
    # 无论发送成功还是失败都要退出你的QQ邮箱
    srv.quit()