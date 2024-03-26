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
scapy模块sr1()方法
"""

# 导包
from scapy.all import *

# 1 发送数据包
# 1-1 构建数据包
# 构建一个嵌套数据包
my_pkg = IP(dst="192.168.43.13") / ICMP()
print(my_pkg.show())  # 查看数据包的详细信息

# 1-2发送数据包
# 基本格式
# sr1(包对象，iface 网卡名)
result = sr1(my_pkg)  # Sent 5 packets.
print(type(result))  # <class 'scapy.layers.inet.IP'>
print(result)  # IP / ICMP 192.168.43.13 > 192.168.43.13 echo-reply 0

# 查看详细信息
print(result.fields)  # 字典格式
print(result.show())  # 获取数据包的详细信息
print(result.summary())  # 获取数据包的简要信息
# print(result['Padding'].load)  # 获取指定端里面的属性信息



