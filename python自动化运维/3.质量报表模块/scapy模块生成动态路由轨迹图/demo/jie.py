"""
title = ''
author = 'huifenghechang'
mtime = '2024/2/27'
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
解析数据包
"""
from scapy.all import *

dpkt = sniff(iface="wlan", count=10)
# wrpcap("mypack.pcap",dpkt)
print(dpkt)
for item in dpkt:
    print(item)
    print("time", item.time)
    print("fields", item.fields)
    print("overload_fields", item.overload_fields)
    print("fields", item.fields)
    print("payload", item.payload)
    print("wirelen", item.wirelen)
    print("==============")
