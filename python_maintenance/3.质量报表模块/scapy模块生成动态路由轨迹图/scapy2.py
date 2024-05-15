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
使用scapy编写简单的端口扫描
"""

import time
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr1


def scan(ip):
    try:
        packet = IP(dst=ip) / TCP(flags="A",
                                  dport=3306)  # 构造标志为ACK的数据包，通过调用TCP将构造好的请求包发送到目的地址，并根据目的地址的响应数据包中的flags字段值判断主机是否存活，若flags字段为R，其整型数值为4时表示接收
        response = sr1(packet)
        if response:
            if int(response[TCP].flags) == 4:
                time.sleep(0.1)
                print(ip + ' ' + 'is up')
            else:
                print(ip + ' ' + 'is down')
        else:
            print(ip + ' ' + 'is down')
    except:
        pass


scan('192.168.2.46')