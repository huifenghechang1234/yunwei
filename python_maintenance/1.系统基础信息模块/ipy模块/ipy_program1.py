"""
title = ''
author = 'huifenghechang'
mtime = '2023/12/10'
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
from IPy import IP

ip_s = input("Please input an IP or net_range:")  # 接收用户输入，参数为ip地址或网络地址
ips = IP(ip_s)
if len(ips) > 1:
    print("---您输入的是一个网络地址---")
    print(f'net:{ips.net()}')  # 输出网络地址
    print(f'netmask:{ips.netmask()}')  # 输出网络掩码地址
    print(f'broadcast: {ips.broadcast()}')  # 输出网络广播地址
    print(f'reverse address:  {ips.reverseNames()[0]}')  # 输出网络方向解析
    print(f'subnet: {len(ips)}')  # 输出网络子网数
else:  # 为单个ip地址
    print("---您输入的是单个IP地址---")
    print(f'reverse address:{ips.reverseNames()[0]}')  # 输出ip反向解析

print(f'hexadecimal: {ips.strHex()}')  # 输出十六进制地址
print(f'binary ip: {ips.strBin()}')  # 输出二进制地址
print(f'iptype:{ips.iptype()}')  # 输出二进制地址