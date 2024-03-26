# -*- coding: utf-8 -*-
import smtplib
import chardet
import codecs
import os
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

# 第三方 SMTP 服务
class txtMail(object):

    def __init__(self, host=None, auth_user=None, auth_password=None):
        self.host = "smtp.163.com" if host is None else host  # 设置发送邮件服务器
        self.auth_user = "somezz" if auth_user is None else auth_user  # 上线时使用专用报警账户的用户名
        self.auth_password = (
            "wqzz2123" if auth_password is None else auth_password
        )  # 上线时使用专用报警账户的密码
        self.sender = "somezz@163.com"

    def send_mail(self, subject, msg_str, recipient_list, attachment_list=None):
        message = MIMEMultipart()
        message["From"] = self.sender
        message["To"] = Header(";".join(recipient_list), "utf-8")
        message["Subject"] = Header(subject, "utf-8")
        message.attach(MIMEText(msg_str, "plain", "utf-8"))

        # 如果有附件，则添加附件
        if attachment_list:
            for att in attachment_list:
                attachment = MIMEText(open(att, "rb").read(), "base64", "utf-8")
                attachment["Content-Type"] = "application/octet-stream"
                # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
                # attname=att.split("/")[-1]
                filename = os.path.basename(att)
                # attm["Content-Disposition"] = 'attachment; filename=%s'%attname
                attachment.add_header(
                    "Content-Disposition",
                    "attachment",
                    filename=("utf-8", "", filename),
                )
                message.attach(attachment)

        smtpObj = smtplib.SMTP_SSL()
        smtpObj.connect(self.host, smtplib.SMTP_SSL_PORT)
        smtpObj.login(self.auth_user, self.auth_password)
        smtpObj.sendmail(self.sender, recipient_list, message.as_string())
        smtpObj.quit()
        print("邮件发送成功")

    def guess_chardet(self, filename):
        """
        :param filename: 传入一个文本文件
        :return:返回文本文件的编码格式
        """
        encoding = None
        try:
            # 由于本需求所解析的文本文件都不大，可以一次性读入内存
            # 如果是大文件，请读取固定字节数
            raw = open(filename, "rb").read()
            if raw.startswith(codecs.BOM_UTF8):  # 处理 UTF-8 with BOM
                encoding = "utf-8-sig"
            else:
                result = chardet.detect(raw)
                encoding = result["encoding"]
        except:
            pass
        return encoding

    def txt_send_mail(self, filename):
        '''
        :param filename:
        :return:
        将指定格式的txt文件发送至邮件，txt文件样例如下
        someone1@xxx.com,someone2@xxx.com...#收件人，逗号分隔
        xxx程序报警   #主题
        程序xxx步骤yyy执行报错，错误代码zzz #正文
        详细信息请看附件   #正文
        file1,file2      #附件，逗号分隔，非必须
        '''

        with open(filename, encoding=self.guess_chardet(filename)) as f:
            lines = f.readlines()
        recipient_list = lines[0].strip().split(",")
        subject = lines[1].strip()
        msg_str = "".join(lines[2:])
        attachment_list = []
        for file in lines[-1].strip().split(","):
            if os.path.isfile(file):
                attachment_list.append(file)
        #如果没有附件，则为None
        if attachment_list == []:
            attachment_list = None
        self.send_mail(
            subject=subject,
            msg_str=msg_str,
            recipient_list=recipient_list,
            attachment_list=attachment_list,
        )


if __name__ == "__main__":
    mymail = txtMail()
    mymail.txt_send_mail(filename="./test.txt")

