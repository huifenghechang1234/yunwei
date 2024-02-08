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
发送HTML格式邮件
本示例通过引入email.mime的MIMEText类来实现支持HTML格式的邮件，支持所有HTML元素，
包含表格、图片、动画、CSS样式、表单等。使用HTML的表格定制美观的业务报表
"""

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# 发件人
from_name = "Hehuyi_In"
# 发件邮箱
from_addr = "xxxxxxx@qq.com"
# 发件邮箱授权码，注意不是QQ邮箱密码
from_pwd = "jjjjjjj"
# 收件邮箱
to_addr = "xxxxxxx@qq.com"

# 邮件标题
my_title = "HTML Test"
# 邮件正文，html格式
my_msg = '''
    <table width="800" border="0" cellspacing="0" cellpadding="4">
      <tr>
          <td bgcolor="#CECFAD" height="20" style="font-size:14px">*官网数据 <a href="monitor.domain.com">更多>></a></td>
      </tr>
      <tr>
        <td bgcolor="#EFEBDE" height="100" style="font-size:13px">
        1）日访问量:<font color=red>152433</font> 访问次数:23651 页面浏览量:45123 点击数:545122 数据流量:504Mb<br>
        2）状态码信息<br>
        &nbsp;&nbsp;500:105 404:3264 503:214<br>
        3）访客浏览器信息<br>
        &nbsp;&nbsp;IE:50% firefox:10% chrome:30% other:10%<br>
        4）页面信息<br>
        &nbsp;&nbsp;/index.php 42153<br>
        &nbsp;&nbsp;/view.php 21451<br>
        &nbsp;&nbsp;/login.php 5112<br>
        </td>
      </tr>
    </table>'''

# 参数2改为html
msg = MIMEText(my_msg, 'html', 'utf-8')
msg['From'] = formataddr([from_name, from_addr])
# 邮件的标题
msg['Subject'] = my_title

# SMTP服务器地址
smtp_srv = "smtp.qq.com"

try:

    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)

    # 使用授权码登录QQ邮箱
    srv.login(from_addr, from_pwd)

    # 使用sendmail方法来发送邮件
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    print('发送成功')
except Exception as e:
    print('发送失败')
finally:
    # 无论发送成功还是失败都要退出你的QQ邮箱
    srv.quit()
