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
本次实践通过 python-nmap 实现一个高效的端口扫描工具，与定时作业crontab 及
邮件告警结合，可以很好地帮助我们及时发现异常开放的高危端口。当然，该工具也可
以作为业务服务端口的可用性探测，例如扫描 192.168.1.20-25 网段 Web 服务端口 80是
否处于open 状态。实践所采用的scan()方法的arguments 参数指定为“-v-PE -p+端
，-v 表示启用细节模式，可以返回非 up 状态主机清单;-PE 表示采用TCP 同步扫描
口”(TCP SYN)方式;-p 指定扫描端口范围。程序输出部分采用了三个 for 循环体，第一层
遍历扫描主机，第二层为遍历协议，第三层为遍历端口，最后输出主机状态
"""
import sys
import nmap

scan_row = []
input_data = input('Please input hosts and port:')
scan_row = input_data.split(" ")
if len(scan_row) != 2:
    print("Input errors,example \"192.168.1.0/24 80,443,22\"")
    sys.exit(0)

hosts = scan_row[0]  # 接收用户输入的主机
port = scan_row[1]  # 接收用户输入的端口
try:
    nm = nmap.PortScanner()  # 创建端口扫描对象
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(0)
except:
    print('Unexpected error:",sys.exc_info()[0]')
    sys.exit(0)

try:
    # 调用扫描方法，参数指定扫描主机 hosts，nmap 扫描命令行参数arguments
    nm.scan('hosts-hosts, arquments= -v -sS -p' + port)
except Exception as e:
    print("Scan erro:" + str(e))

for host in nm.all_hosts():  # 遍历扫描主机
    print('Host : %s (8s)'(host, nm[host].hostname()))  # 输出主机及主机名
    print('State :%s' % nm[host].state())  # 输出主机状态，如up、down

for proto in nm[host].all_protocols():  # 遍历扫描协议，如tcP、udp
    print('----------')
    print('Protocol : %s' % proto)  # 输入协议名

    lport = nm[host][proto].keys()  # 获取协议的所有扫描瑞口
    lport.sort()  # 端口列表排序

    for port in lport:  # 遍历端口及输出端口与状态
        print('port :ststate :s'(port, nm[host][proto][port]['state']))
