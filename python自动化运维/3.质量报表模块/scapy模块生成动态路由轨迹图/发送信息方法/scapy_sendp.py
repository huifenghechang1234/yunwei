"""
title = ''
author = 'huifenghechang'
mtime = '2024/2/25'
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
scapy模块sendp()方法
"""

# 导包
from scapy.all import *

# 1 发送数据包
# 1-1 构建数据包
# 构建一个嵌套数据包
http_data = "hello world"
my_pkg = Ether(dst="00:50:56:C0:00:08") / IP(dst="192.168.43.13") / TCP(dport=53) / http_data
print(my_pkg.show())  # 查看数据包的详细信息

# 1-2发送数据包
# 基本格式
# send(包对象，inter=间隔时间，count=发送数量)
result = sendp(my_pkg, inter=1, count=5)  # Sent 5 packets.
print(type(result))  # <class 'NoneType'>
print(result)  # None  send仅仅是发送数据，不接收数据，所以没有信息