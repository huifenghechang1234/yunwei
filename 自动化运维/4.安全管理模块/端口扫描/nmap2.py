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
"""
单个IP扫描
"""

import nmap  # 导入 nmap.py 模块

nm = nmap.PortScanner()  # 获取 PortScanner 对象

nm.scan('127.0.0.1', '22-443')  # 扫描主机 127.0.0.1 端口号 22-443

nm.command_line()  # 获取用于扫描的命令行：nmap -oX - -p 22-443 127.0.0.1

nm.scaninfo()  # 获取本次扫描的信息 {'tcp': {'services': '22-443', 'method': 'connect'}}

nm.all_hosts()  # 获取所有扫描到的主机

nm['127.0.0.1'].hostname()  # 获取 127.0.0.1 的主机名

nm['127.0.0.1'].hostnames()  # 获取list格式的主机名dict 127.0.0.1 # 如 [{'name':'hostname1', 'type':'PTR'}, {'name':'hostname2', 'type':'user'}]

nm['127.0.0.1'].state()  # 获取主机 127.0.0.1 的状态 (up|down|unknown|skipped)

nm['127.0.0.1']['tcp'].keys()  # 获取所有tcp端口

nm['127.0.0.1'].all_tcp()  # 获取所有tcp端口 （已排序）

nm['127.0.0.1'].all_udp()  # 同上

nm['127.0.0.1'].all_ip()  # 同上

nm['127.0.0.1'].all_sctp()  # 同上

nm['127.0.0.1'].has_tcp(22)  # 是否含有主机 127.0.0.1 的 22 端口的信息

nm['127.0.0.1']['tcp'][22]  # 获取主机 127.0.0.1 22 端口（tcp）的所有信息

nm['127.0.0.1'].tcp(22)  # 获取主机 127.0.0.1 22 端口的所有信息

