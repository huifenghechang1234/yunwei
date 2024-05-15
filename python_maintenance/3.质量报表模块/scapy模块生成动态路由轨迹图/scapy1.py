"""
title = ''
author = 'huifenghechang'
mtime = '2023/12/28'
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
from scapy.layers.inet import traceroute

"""
scapy模块
scapy是一个可用作网络嗅探，独立运行的工具，它提供了一个和python相同的交互方式命令行环境，可以在kali内单独运行，
该类库在网络安全领域有非常广泛用例，可用于漏洞利用开发、流量的分析捕获等等。我们使用这个库实现对网络数据包的发送、
监听和解析，编写可以用进行网络探测扫描的脚本
"""

import time, subprocess
import warnings, logging

warnings.filterwarnings("ignore", category=DeprecationWarning)  # 屏scapy无用告警信息
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # 屏模块IPV6多余告警

domains = input('Please input one or more IP/domain:')  # 接受输入的域名或IP
target = domains.split(' ')
dport = [80]  # 扫描的端口列表

if len(target) >= 1 and target[0] != '':
    res, unans = traceroute(target, dport=dport, retry=-2)  # 启动路由跟踪
    res.graph(target="> test.svq")  # 生成 svq 矢量图形

    time.sleep(1)
    subprocess.Popen("/usr/bin/convert test;svg test,png", Shell=True)  # svg转png格式
else:
    print("IP/domain number of errors,exit")




