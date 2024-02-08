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
判断主机是否存活
"""

import nmap
nm = nmap.PortScanner()
nm.scan(hosts='172.17.2.0/24', arguments='-n -sP -PE')
up_hosts = nm.all_hosts()		# 获取存活主机列表
print(up_hosts)
