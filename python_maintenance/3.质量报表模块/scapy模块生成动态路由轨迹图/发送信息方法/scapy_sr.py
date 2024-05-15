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
scapy模块sr()方法
"""

# 导包
from scapy.all import *

# 1 发送数据包
# 1-1 构建数据包
# 构建一个嵌套数据包
http_data = "hello world"
my_pkg = Ether(dst="00:50:56:C0:00:08") / IP(dst="192.168.43.13") / TCP(dport=53) / http_data
print(my_pkg.show())  # 查看数据包的详细信息

print("*******************2******************************")
# 1-2发送数据包
# 基本格式
# send(包对象，inter=间隔时间，count=发送数量)
result = sr(my_pkg, inter=1)
print(type(result))  # <class 'tuple'>
print(result)  # 查看基本的返回信息条目 (<Results: TCP:0 UDP:0 ICMP:0 Other:0>, <Unanswered: TCP:1 UDP:0 ICMP:0 Other:0>)

print("*********************3****************************")
# 1-3 查看返回信息
print(result[0])  # 根据切片方式来获取具体的数据信息
print(result[1])
print(type(result[1]))  # PacketList 类型数据

print("**********************4***************************")
# 1-4 信息详情
# # res 属性 用于获取应答数据的结果
print(result[1].res)
print(type(result[1].res))  # <class list'> 类型数据
# print(result[1].res[1]) # res后面的索引是基于数据包来定制的
print(result[1].res[0])  # res后面的索引是基于数据包来定制的
print(type(result[1].res[0]))  # 表示这些数据是二进制的

print("***********************5**************************")
# #1-5数据包的信息
# # fields - 查看所有的字段信息
# show()/summary/summary
print(result[1].res[0].fields)
print(result[1].res[0].show)
print(type(result[1].res[0].show))

print("***********************6**************************")
# 信息获取的方式: [索引值]，[名称]
print(result[1].res[0][1])  # 获取Ethernet里面的数据
print(result[1].res[0][3])  # 获取Raw里面的数据

print("**********************7***************************")
# 查看ip相关数据信息
print(result[1].res[0]['IP'].fields)  # 这是一个字典格式
print(result[1].res[0]['IP'].dst)  # 通过字典属性的方式获取具体的ip信息








