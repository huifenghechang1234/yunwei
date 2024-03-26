# -*- encoding:utf-8 -*-
import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

# 输入邮件地址, 口令和POP3服务器地址
email = "somenzz@qq.com"
password = "huerwgigwcvdbbfh"
pop3_server = "pop.qq.com"


# 连接到POP3服务器,如果开启ssl请使用poplib.POP3_SSL
server = poplib.POP3_SSL(pop3_server)
# 可以打开或关闭调试信息
# server.set_debuglevel(1)
# 可选:打印POP3服务器的欢迎文字
print(server.getwelcome().decode("utf-8"))

# 身份认证:
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间:
print("邮件数量: %s个. 大小: %.2fMB" % (server.stat()[0], server.stat()[1] / 1024 / 1024))


# list()返回所有邮件的编号:
resp, mails, octets = server.list()
# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]


# 获取最新一封邮件, 注意索引号从1开始,最新的邮件索引即为邮件的总个数
index = len(mails)
resp, lines, octets = server.retr(index)

# lines存储了邮件的原始文本的每一行可以获得整个邮件的原始文本
msg_content = b"\r\n".join(lines).decode("utf-8")
# 稍后解析出邮件
msg = Parser().parsestr(msg_content)


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


print("解析获取到的邮件内容如下：\n----------begin------------")
# 打印发件人信息
print(
    f"{ decode_str(parseaddr(msg.get('From',''))[0])}<{decode_str(parseaddr( msg.get('From',''))[1])}>"
)
# 打印收件人信息
print(
    f"{ decode_str(parseaddr(msg.get('To',''))[0])}<{decode_str(parseaddr( msg.get('To',''))[1])}>"
)
# 打印主题信息
print(decode_str(msg["Subject"]))
# 打印第一条正文信息
part0 = msg.get_payload()[0]
content = part0.get_payload(decode=True)
print(content.decode(part0.get_content_charset()))
print("----------end------------")

# 可以根据邮件索引号直接从服务器删除邮件
# server.dele(index)
# 关闭连接:
server.quit()
