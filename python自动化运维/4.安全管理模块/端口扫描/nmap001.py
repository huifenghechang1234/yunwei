"""
title = ''
author = 'huifenghechang'
mtime = '2024/3/3'
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
python的nmap模块
在Python中，有一个名为python-nmap的模块，它是一个用于网络扫描和主机发现的工具。python-nmap模块是对Nmap
的Python封装，可以通过Python代码调用Nmap进行网络扫描，并分析扫描结果

python-nmap模块的常见功能：
执行Nmap扫描：python-nmap模块允许你执行各种类型的Nmap扫描，包括TCP扫描、UDP扫描、OS检测、服务版本检测等。
解析扫描结果：一旦扫描完成，python-nmap模块可以帮助你解析Nmap扫描的结果，提取目标主机的IP地址、开放的端口、服务版本信息等。
灵活性：你可以使用python-nmap模块自定义扫描选项，包括扫描的端口范围、扫描的目标主机、扫描的速度等。
多种输出格式：python-nmap模块支持将扫描结果以不同的格式输出，包括文本格式、JSON格式等

首先导入了nmap模块。然后，我们创建了一个PortScanner对象，用于执行Nmap扫描。接着，我们使用scan()方法执行TCP SYN
扫描，并指定了扫描的目标主机和端口范围。最后，我们遍历扫描结果，并输出了扫描结果中的主机状态、协议和端口状态等信息
"""

import nmap

# 创建一个Nmap扫描器对象
nm = nmap.PortScanner()

# 执行TCP SYN扫描
# nm.scan('127.0.0.1', '22-443')
nm.scan('www.baidu.com', '1-1024')

# 输出扫描结果
for host in nm.all_hosts():
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())

    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)

        lport = list(nm[host][proto].keys())  # 将 nm[host][proto].keys() 转换为列表，然后使用 sort() 方法对列表进行排序
        lport.sort()
        for port in lport:
            print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))


"""
Host : 183.2.172.185 (www.baidu.com)
State : up
----------
Protocol : tcp
port : 80	state : open
port : 443	state : open
"""