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
srp方法
"""
from scapy.all import *

# 构造数据包
my_pkg = Ether(dst='ff:ff:ff:ff:ff:ff')/ ICMP()

# 发送数据包
result = srp(my_pkg, timeout=1, verbose=True)

# 查看数据包
print("****************1***********************")
print(result)
print("****************2***********************")
print(result[1].res)
print("****************3***********************")
print(result[1].res[0].show())
print("*****************4**********************")
print(result[1].res[0][1].fields)
print("******************5*********************")
print(result[1].res[0]['ICMP'])



