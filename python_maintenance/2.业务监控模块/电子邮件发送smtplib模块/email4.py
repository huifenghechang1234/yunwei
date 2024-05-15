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
发送带附件的邮件
本示例通过MIMEText与MIMEImage类的组合，实现图文邮件格式，
另通过MIMEText类再定义Content-Disposition属性来实现带附件的邮件

实践步骤：
1.准备附件文件
2.定制附件对象
3.增加附件对象
4.查看效果

MIMEText 类通常用于创建文本类型的 MIME 对象，而不是用于附加二进制文件（如文档或图片）。
当您想要附加非文本文件时，应该使用 MIMEBase 或其子类 MIMEApplication

附件的基本操作
1 attach = MIMEText(open("doc/mysql_data.xlsx"rb').read()，"base64"，'utf-8')
2 attach['Content-Type'] = "application/octet-stream'
3 attach.add _header ('Content-Disposition', "attachment '.filename=("utf-8"，""，"我的数据库数据.x1sx"))
结果显示:2和3基本上都是定制的，不会变动太多

其他的附件操作
MIMEText(open('text1.txt',"rb').read0)，"base64 ，"utf-8')    文本
MIMEText (open(123.jpg','rb').read()，"base64'，"utf-8')      图片
MIMEText(open('report_test.html ，'rb').read0，"base64',utf-8')     附件

批量添加附件
attach = MIMEText (open("file_name"，'rb').read0，"base64",utf-8')
attach['Content-Type'] = "application/octet-stream"
attach['Content-Disposition'] = 'attachment;filename="file_name"
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import formataddr

# 发件人
from_name = "Hehuyi_In"
# 发件邮箱
from_addr = "2213024107@qq.com"
# 发件邮箱授权码，注意不是QQ邮箱密码
from_pwd = "vrvwleaezcrnecih"
# 收件邮箱
to_addr = "2213024107@qq.com"
# 邮件标题
my_title = "Text+Image+Attachment Test"


# 添加图片函数，参数1：图片路径，参数2：图片id
def addimg(src, imgid):
    fp = open(src, 'rb')  # 打开文件
    msg_image = MIMEImage(fp.read())  # 创建MIMEImage对象，读取图片内容并作为参数
    fp.close()  # 关闭文件
    msg_image.add_header('Content-ID', imgid)  # 指定图片文件的Content-ID,<img>标签src用到
    return msg_image


# 创建MIMEMultipart对象，采用related定义内嵌资源的邮件体
msg_multipart = MIMEMultipart('related')

# 创建一个MIMEText对象，HTML元素包括文字与图片<img>
msg_text = MIMEText("<font color=red>sqlserver介绍<br><img src=\"cid:001\" border=\"1\"><br>详情参考附件</font>",
                    "html", "utf-8")

# 创建附件对象
# 创建一个MIMEText对象，附加sqlserver.txt文档
msg_attach = MIMEText(open("doc/sqlserver.txt", "rb").read(), "base64", "utf-8")

# 指定文件格式类型
msg_attach["Content-Type"] = "application/octet-stream"

# 指定Content-Disposition值为attachment则出现下载保存对话框，保存的默认文件名使用filename指定
msg_attach["Content-Disposition"] = "attachment; filename=\"sqlserver.txt\""

# 解决中文问题
msg_attach.add_header("Content-Disposition", "attachment", filename=("utf-8", "", "sqlserver1.txt"))

# MIMEMultipart对象附加text,img,attach内容
msg_multipart.attach(msg_text)
msg_multipart.attach(addimg("img/001.png", "001"))  # 图片路径与标签，001对应上方html中的<img src="cid:001">
msg_multipart.attach(msg_attach)

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
    # 打印具体报错
    print(e)
finally:
    # 无论发送成功还是失败都要退出你的QQ邮箱
    srv.quit()
