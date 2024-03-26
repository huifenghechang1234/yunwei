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
抓包sniff方法
"""
from scapy.all import *

package = sniff(iface='ens33', count=10)  # 扫描ens33网卡的数据包，总数为10个
print(package)  # 查看抓取的数据包
print(package[0])  # 查看默认第一个数据包的数据

print(package[0].show())  # 查看默认第一个数据包的详情

wrpcap("test.pcap", package)  # 将抓取到的包保存为test.pcap文件
# 注意: 抓包需要依赖于ping 192.168.8.12 -c1 的动作
