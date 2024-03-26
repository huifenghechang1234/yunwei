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

# 定义ip网段
ip = IP("192.168.0.0/16")
# 打印输出该网段的ip个数
print('1.该网段ip数：', ip.len())
# 循环遍历打印输出ip
# for x in ip:
#	print(x)

# 反向解析地址格式
ip = IP('192.168.1.130')
reverse = ip.reverseName()
print("2.反向解析地址格式：", reverse)
# 获取地址类型
typeIP = ip.iptype()
print('3.获取地址类型：', typeIP)
print(IP('8.8.8.8').iptype())
# 转换成整型格式
print('4.整型格式转换：', ip.int())
print('5.二进制格式转换：', ip.strBin())
print('6.十六进制格式转换：', ip.strHex())
print('7.十六进制转换成ip:', IP(0xc0a80182))

# 根据ip和掩码生成网段格式
print('8.根据ip和掩码生成网段格式：', IP('192.168.1.0').make_net('255.255.255.0'))
print(IP('192.168.2.0/255.255.255.0', make_net=True))
print(IP('192.168.3.0-192.168.3.255', make_net=True))

# strNormal
print('9.strNormal')
# 无返回值
print(IP('192.168.1.0/24').strNormal(0))
# prefix格式
print(IP('192.168.2.0/24').strNormal(1))
# decimalnetmask格式
print(IP('192.168.3.0/24').strNormal(2))
# lastIP格式
print(IP('192.168.4.0/24').strNormal(3))

# 比较两个网段是否重叠 包含
print('10.比较大小：')
ip1 = IP('192.168.1.0/24')
ip2 = IP('182.168.1.0/24')
# 数值类型的比较
print(ip1 > ip2)
# 判断包含
print('11.判断包含:')
print(IP('192.168.1.12') in IP('192.168.1.0/24'))
print(IP('192.168.1.0/24') in IP('192.168.0.0/16'))

# overlaps  1表示重叠 0不存在重叠
print('12.判断重叠：')
print(IP('192.168.0.0/23').overlaps('192.168.1.0/24'))
print(IP('192.168.1.0/24').overlaps('192.168.2.0/24'))
# 区分ipv4与ipv6
print('区分ipv4与ipv6:')
print(IP('10.0.0.0/8').version())
print(IP('::1').version())
