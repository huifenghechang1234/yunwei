"""
title = ''
author = 'huifenghechang'
mtime = '2023/11/29'
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
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-u", "--user", action="store_true", dest="users", default=False, help="user names")
parser.add_option("-p", "--port", action="store_true", dest="ports", default=False, help="user ports")
(options, args) = parser.parse_args()

if options.users == True:
    print("user names is true")
if options.ports == True:
    print("passwd is true")


#  1.批量遍历目录文件,并修改访问时间
import os

path = "D:/UASM64/include/"
dirs = os.listdir(path)
temp = [];

for file in dirs:
    temp.append(os.path.join(path, file))
for x in temp:
    os.utime(x, (1577808000, 1577808000))


#  2.遍历目录和文件
import os

def list_all_files(rootdir):
    import os
    _files = []    # 字典
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):   #  遍历
        path = os.path.join(rootdir, list[i])
        if os.path.isdir(path):
            _files.extend(list_all_files(path))
        if os.path.isfile(path):
            _files.append(path)
    return _files

a = list_all_files("C:/Users/LyShark/Desktop/a")
print(a)


#  3.检测指定端口状态

import socket

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.settimeout(1)

for ip in range(0,254):
    try:
        sk.connect(("192.168.1."+str(ip),443))
        print("192.168.1.%d server open \n"%ip)
    except Exception:
        print("192.168.1.%d server not open"%ip)

sk.close()


#  4.实现批量执行CMD命令

import sys
import os
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print("------------------------------>\n")
print("使用说明,在当前目录创建ip.txt写入ip地址")
print("------------------------------>\n")

user=input("输入用户名:")
passwd=input("输入密码:")
port=input("输入端口:")
cmd=input("输入执行的命令:")

file = open("./ip.txt", "r")
line = file.readlines()

for i in range(len(line)):
        print("对IP: %s 执行"%line[i].strip('\n'))

        ssh.connect(hostname=line[i].strip('\n'),port=port,username=user,password=passwd)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()

        if not result:
            result=stderr.read()
        ssh.close()

        print(result.decode())



# 5. 实现钉钉报警

import requests
import sys
import json

dingding_url = 'https://oapi.dingtalk.com/robot/send?access_token=6d11af3252812ea50410c2ccb861814a6ed11b2306606934a5d4ca9f2ec8c09'

data = {"msgtype": "markdown","markdown": {"title": "监控","text": "apche异常"}}

headers = {'Content-Type':'application/json;charset=UTF-8'}

send_data = json.dumps(data).encode('utf-8')
requests.post(url=dingding_url,data=send_data,headers=headers)

# coding: utf-8
import psutil
import requests
import time
import os
import json

monitor_name = set(['httpd', 'cobblerd'])  # 用户指定监控的服务进程名称

proc_dict = {}
proc_name = set()  # 系统检测的进程名称
monitor_map = {
    'httpd': 'systemctl restart httpd',
    'cobblerd': 'systemctl restart cobblerd'  # 系统在进程down掉后，自动重启
}

dingding_url = 'https://oapi.dingtalk.com/robot/send?access_token=b5258c4335ed8ab792075013c965efcbf4f8940f92e7bd936cdc7842d3bf9405'
# 钉钉机器人token使用参考文档：http://www.pc6.com/infoview/Article_108931.html

while True:
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        proc_dict[proc.info['pid']] = proc.info['name']
        proc_name.add(proc.info['name'])

    proc_stop = monitor_name - proc_name  # 通过集合的形式来找出停掉的进程名,前者有但是后者没有的

    if proc_stop:  # 如果确实有监控的进程停掉了，那么我们需要告警以及自动重启功能
        for p in proc_stop:
            p_status = '停止'
            p_name = p
            data = {
                "msgtype": "markdown",
                "markdown": {
                    "title": "监控信息",
                    "text": "### %s\n" % time.strftime("%Y-%m-%d %X") +
                            "> #### 服务名：%s \n\n" % p_name +
                            "> #### 状态：%s \n\n" % p_status +
                            "> #### 正在尝试启动"
                },
            }
            headers = {'Content-Type': 'application/json;charset=UTF-8'}
            send_data = json.dumps(data).encode('utf-8')
            requests.post(url=dingding_url, data=send_data, headers=headers)

            os.system(monitor_map[p_name])  # 执行重启命令，然后判断是否重启成功
            proc_set = set()
            for proc_again in psutil.process_iter(attrs=['pid', 'name']):
                proc_set.add(proc_again.info['name'])

            if p in proc_set:  # 如果进程启动成功，p是以前停掉的进程，proc_set是已经重启过一次后的所有进程集合
                p_status = '成功'
                p_name = p
                data = {
                    "msgtype": "markdown",
                    "markdown": {
                        "title": "监控信息",
                        "text": "### %s\n" % time.strftime("%Y-%m-%d %X") +
                                "> #### 服务名：%s \n\n" % p_name +
                                "> #### 状态：%s \n\n" % p_status +
                                "> #### 已经启动成功，服务正在运行！"
                    },
                }
                headers = {'Content-Type': 'application/json;charset=UTF-8'}
                send_data = json.dumps(data).encode('utf-8')
                requests.post(url=dingding_url, data=send_data, headers=headers)
            else:
                p_status = '重启失败'
                p_name = p
                data = {
                    "msgtype": "markdown",
                    "markdown": {
                        "title": "监控信息",
                        "text": "### %s\n" % time.strftime("%Y-%m-%d %X") +
                                "> #### 服务名：%s \n\n" % p_name +
                                "> #### 状态：%s \n\n" % p_status +
                                "> #### Sorry,服务启动失败鸟！"
                    },
                }
                headers = {'Content-Type': 'application/json;charset=UTF-8'}
                send_data = json.dumps(data).encode('utf-8')
                requests.post(url=dingding_url, data=send_data, headers=headers)
    time.sleep(5)


#  6.判断指定端口是否开放
import socket

port_number = [135,443,80]

for index in port_number:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', index))
    if result == 0:
        print("Port %d is open" % index)
    else:
        print("Port %d is not open" % index)
    sock.close()


# 7. 判断指定端口并且实现钉钉轮询报警
import requests
import sys
import json
import socket
import time

def dingding(title,text):
    dingding_url = 'https://oapi.dingtalk.com/robot/send?access_token=6d11af3252812ea50410c2ccb861814a69ed11b2306606934a5d4ca9f2c8c09'
    data = {"msgtype": "markdown","markdown": {"title": title,"text": text}}
    headers = {'Content-Type':'application/json;charset=UTF-8'}
    send_data = json.dumps(data).encode('utf-8')
    requests.post(url=dingding_url,data=send_data,headers=headers)

def net_scan():
    port_number = [80,135,443]
    for index in port_number:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', index))
        if result == 0:
            print("Port %d is open" % index)
        else:
            return index
        sock.close()

while True:
    dingding("Warning",net_scan())
    time.sleep(60)


# 8.实现SSH批量CMD执行命令
import sys
import os
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def ssh_cmd(user,passwd,port,userfile,cmd):
    file = open(userfile, "r")
    line = file.readlines()
    for i in range(len(line)):
        print("对IP: %s 执行"%line[i].strip('\n'))
        ssh.connect(hostname=line[i].strip('\n'),port=port,username=user,password=passwd)
        cmd=cmd
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()

        if not result:
            result=stderr.read()
        ssh.close()

        print(result.decode())

ssh_cmd("lyshark","123","22","./ip.txt","free -h |grep 'Mem:' |awk '{print $3}'")


# 9.列举当前目录以及所有子目录下的文件，并打印出绝对路径
import sys
import os

for root,dirs,files in os.walk("C://"):
    for name in files:
        print(os.path.join(root,name))
os.walk()


# 10.按照这样的日期格式(xxxx-xx-xx)每日生成一个文件，例如今天生成的文件为2013-09-23.log， 并且把磁盘的使用情况写到到这个文件中
import os
import sys
import time

new_time = time.strftime("%Y-%m-%d")
disk_status = os.popen("df -h").readlines()

str1 = ''.join(disk_status)
f = open(new_time+'.log','w')
f.write("%s"%str1)

f.flush()
f.close()


# 11.统计出每个IP的访问量有多少
import sys

list = []

f = open("/var/log/httpd/access_log","r")
str1 = f.readlines()
f.close()

for i in str1:
        ip=i.split()[0]
        list.append(ip)

list_num=set(list)

for j in list_num:
        num=list.count(j)
        print("%s -----> %s" %(num,j))


# 12.接受用户输入数字，并进行校验，非数字给出错误提示，然后重新等待用户输入，根据用户输入数字，输出从0到该数字之间所有的素数。(只能被1和自身整除的数为素数)
# import tab
import sys

while True:
        try:
                num=int(input("输入数字：").strip())
                for x in range(2,num+1):
                        for y in range(2,x):
                                if x % y == 0:
                                        break
                                else:
                                        print(x)
        except ValueError:
                print("您输入的不是数字")
        except KeyboardInterrupt:
                sys.exit("\n")


# 12.查看进程的内存占用大小，写一个脚本计算一下所有进程所占用内存大小的和
import sys
import os

list=[]
sum=0

str1=os.popen("ps aux","r").readlines()

for i in str1:
        str2=i.split()
        new_rss=str2[5]
        list.append(new_rss)
for i in list[1:-1]:
        num=int(i)
        sum=sum+num

print("%s ---> %s"%(list[0],sum))



# 13.命令行参数argv

import sys

if len(sys.argv) < 2:
    print("没有输入任何参数")
    sys.exit()

if sys.argv[1].startswith("-"):
    option = sys.argv[1][1:]

    if option == "version":
        print("版本信息")
    elif option == "help":
        print("帮助菜单")
    elif option == "option":
        print("配置菜单")
    else:
        print("异常")
        sys.exit()


#  14.用random生成6位数字加字母随机验证码

import sys
import random

rand = []

for x in range(6):
    y = random.randrange(0, 5)
    if y == 2 or y == 4:
        num = random.randrange(0, 9)
        rand.append(str(num))
    else:
        temp = random.randrange(65, 91)
        c = chr(temp)
        rand.append(c)
result = "".join(rand)
print(result)


# 15.使用pexpect非交互登陆系统

import pexpect
import sys

ssh = pexpect.spawn('ssh lyshark@59.110.167.239')
fout = file('sshlog.txt', 'w')
ssh.logfile = fout

ssh.expect("lyshark@59.110.167.239's password:")

ssh.sendline("密码")
ssh.expect('#')

ssh.sendline('ls /home')
ssh.expect('#')


# 16.取系统时间

import sys
import time

time_str = time.strftime("日期：%Y-%m-%d", time.localtime())
print(time_str)

time_str = time.strftime("时间：%H:%M", time.localtime())
print(time_str)


#17. 获取内存使用情况

import sys
import os
import psutil


# 18.获取系统内存使用情况

memory_convent = 1024 * 1024
mem = psutil.virtual_memory()

print("内存容量为:" + str(mem.total / (memory_convent)) + "MB\n")
print("已使用内存:" + str(mem.used / (memory_convent)) + "MB\n")
print("可用内存:" + str(mem.total / (memory_convent) - mem.used / (1024 * 1024)) + "MB\n")
print("buffer容量:" + str(mem.buffers / (memory_convent)) + "MB\n")
print("cache容量:" + str(mem.cached / (memory_convent)) + "MB\n")


# 19.通过SNMP协议监控CPU，被监控的机器上需要支持snmp协议
# yum
# install - y
# net - snmp *

# !/usr/bin/python
import os


def getAllitems(host, oid):
    sn1 = os.popen('snmpwalk -v 2c -c public ' + host + ' ' + oid + '|grep Raw|grep Cpu|grep -v Kernel').read().split(
        '\n')[:-1]
    return sn1


def getDate(host):
    items = getAllitems(host, '.1.3.6.1.4.1.2021.11')

    date = []
    rate = []
    cpu_total = 0

    # us = us+ni, sy = sy + irq + sirq

    for item in items:
        float_item = float(item.split(' ')[3])
        cpu_total += float_item
        if item == items[0]:
            date.append(float(item.split(' ')[3]) + float(items[1].split(' ')[3]))
        elif item == item[2]:
            date.append(float(item.split(' ')[3] + items[5].split(' ')[3] + items[6].split(' ')[3]))
        else:
            date.append(float_item)

    # calculate cpu usage percentage

    for item in date:
        rate.append((item / cpu_total) * 100)

    mean = ['%us', '%ni', '%sy', '%id', '%wa', '%cpu_irq', '%cpu_sIRQ']

    # calculate cpu usage percentage
    result = map(None, rate, mean)
    return result


if __name__ == '__main__':

    hosts = ['192.168.1.17', '192.168.1.17']

    for host in hosts:
        print
        '==========' + host + '=========='
        result = getDate(host)
        print
        'Cpu(s)',
        # print result
        for i in range(5):
            print
            ' %.2f%s' % (result[i][0], result[i][1]),
        print
        print


# 20.通过SNMP协议监控系统负载，被监控的机器上需要支持snmp协议
# yum
# install - y
# net - snmp *

# !/usr/bin/python
import os
import sys


def getAllitems(host, oid):
    sn1 = os.popen('snmpwalk -v 2c -c public ' + host + ' ' + oid).read().split('\n')
    return sn1


def getload(host, loid):
    load_oids = '1.3.6.1.4.1.2021.10.1.3.' + str(loid)
    return getAllitems(host, load_oids)[0].split(':')[3]


if __name__ == '__main__':

    hosts = ['192.168.1.17', '192.168.1.17']

    print('==============System Load==============')

    for host in hosts:
        load1 = getload(host, 1)
        load10 = getload(host, 2)
        load15 = getload(host, 3)
        print('%s load(1min): %s ,load(10min): %s ,load(15min): %s' % (host, load1, load10, load15))


# 21.通过SNMP协议监控内存，被监控的机器上需要支持snmp协议
# yum
# install - y
# net - snmp *

# !/usr/bin/python
import os


def getAllitems(host, oid):
    sn1 = os.popen('snmpwalk -v 2c -c public ' + host + ' ' + oid).read().split('\n')[:-1]
    return sn1


def getSwapTotal(host):
    swap_total = getAllitems(host, 'UCD-SNMP-MIB::memTotalSwap.0')[0].split(' ')[3]
    return swap_total


def getSwapUsed(host):
    swap_avail = getAllitems(host, 'UCD-SNMP-MIB::memAvailSwap.0')[0].split(' ')[3]
    swap_total = getSwapTotal(host)
    swap_used = str(round(((float(swap_total) - float(swap_avail)) / float(swap_total)) * 100, 2)) + '%'
    return swap_used


def getMemTotal(host):
    mem_total = getAllitems(host, 'UCD-SNMP-MIB::memTotalReal.0')[0].split(' ')[3]
    return mem_total


def getMemUsed(host):
    mem_total = getMemTotal(host)
    mem_avail = getAllitems(host, 'UCD-SNMP-MIB::memAvailReal.0')[0].split(' ')[3]
    mem_used = str(round(((float(mem_total) - float(mem_avail)) / float(mem_total)) * 100, 2)) + '%'
    return mem_used


if __name__ == '__main__':

    hosts = ['192.168.1.17', '192.168.1.17']
    print("Monitoring Memory Usage")

    for host in hosts:
        mem_used = getMemUsed(host)
        swap_used = getSwapUsed(host)

        print('==========' + host + '==========')
        print('Mem_Used = %-15s  Swap_Used = %-15s' % (mem_used, swap_used))
        print()


#22. 通过SNMP协议监控磁盘，被监控的机器上需要支持snmp协议
# yum
# install - y
# net - snmp *

# !/usr/bin/python

import re
import os


def getAllitems(host, oid):
    sn1 = os.popen('snmpwalk -v 2c -c public ' + host + ' ' + oid).read().split('\n')[:-1]
    return sn1


def getDate(source, newitem):
    for item in source[5:]:
        newitem.append(item.split(':')[3].strip())
    return newitem


def getRealDate(item1, item2, listname):
    for i in range(len(item1)):
        listname.append(int(item1[i]) * int(item2[i]) / 1024)
    return listname


def caculateDiskUsedRate(host):
    hrStorageDescr = getAllitems(host, 'HOST-RESOURCES-MIB::hrStorageDescr')
    hrStorageUsed = getAllitems(host, 'HOST-RESOURCES-MIB::hrStorageUsed')
    hrStorageSize = getAllitems(host, 'HOST-RESOURCES-MIB::hrStorageSize')
    hrStorageAllocationUnits = getAllitems(host, 'HOST-RESOURCES-MIB::hrStorageAllocationUnits')

    disk_list = []
    hrsused = []
    hrsize = []
    hrsaunits = []

    # get disk_list

    for item in hrStorageDescr:
        if re.search('/', item):
            disk_list.append(item.split(':')[3])

    # print disk_list

    getDate(hrStorageUsed, hrsused)
    getDate(hrStorageSize, hrsize)

    # print getDate(hrStorageAllocationUnits,hrsaunits)

    # get hrstorageAllocationUnits

    for item in hrStorageAllocationUnits[5:]:
        hrsaunits.append(item.split(':')[3].strip().split(' ')[0])

    # caculate the result

    # disk_used = hrStorageUsed * hrStorageAllocationUnits /1024 (KB)

    disk_used = []
    total_size = []
    disk_used = getRealDate(hrsused, hrsaunits, disk_used)
    total_size = getRealDate(hrsize, hrsaunits, total_size)

    diskused_rate = []

    for i in range(len(disk_used)):
        diskused_rate.append(str(round((float(disk_used[i]) / float(total_size[i]) * 100), 2)) + '%')

    return diskused_rate, disk_list


if __name__ == '__main__':

    hosts = ['192.168.1.17', '192.168.1.17']

    for host in hosts:

        result = caculateDiskUsedRate(host)
        diskused_rate = result[0]
        partition = result[1]

        print("==========", host, '==========')

        for i in range(len(diskused_rate)):
            print('%-20s used: %s' % (partition[i], diskused_rate[i]))
        print()


# 23.通过SNMP协议监控网卡流量，被监控的机器上需要支持snmp协议
# yum
# install - y
# net - snmp *

# !/usr/bin/python

import re
import os


# get SNMP-MIB2 of the devices
def getAllitems(host, oid):
    sn1 = os.popen('snmpwalk -v 2c -c public ' + host + ' ' + oid).read().split('\n')[:-1]
    return sn1


# get network device
def getDevices(host):
    device_mib = getAllitems(host, 'RFC1213-MIB::ifDescr')
    device_list = []

    for item in device_mib:
        if re.search('eth', item):
            device_list.append(item.split(':')[3].strip())
    return device_list


# get network date

def getDate(host, oid):
    date_mib = getAllitems(host, oid)[1:]
    date = []

    for item in date_mib:
        byte = float(item.split(':')[3].strip())
        date.append(str(round(byte / 1024, 2)) + ' KB')
    return date


if __name__ == '__main__':

    hosts = ['192.168.1.17', '192.168.1.17']

    for host in hosts:
        device_list = getDevices(host)
        inside = getDate(host, 'IF-MIB::ifInOctets')
        outside = getDate(host, 'IF-MIB::ifOutOctets')

        print
        '==========' + host + '=========='

        for i in range(len(inside)):
            print
            '%s : RX: %-15s   TX: %s ' % (device_list[i], inside[i], outside[i])
        print


# 24.实现多级菜单

import os
import sys

ps = "[None]->"
ip = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
flage = 1

while True:
    ps = "[None]->"
    temp = input(ps)
    if (temp == "test"):
        print("test page !!!!")
    elif (temp == "user"):
        while (flage == 1):
            ps = "[User]->"
            temp1 = input(ps)
            if (temp1 == "exit"):
                flage = 0
                break
            elif (temp1 == "show"):
                for i in range(len(ip)):
                    print(i)


#25. 检查各个进程读写的磁盘IO

# !/usr/bin/env python
# -*- coding=utf-8 -*-

import sys
import os
import time
import signal
import re


class DiskIO:
    def __init__(self, pname=None, pid=None, reads=0, writes=0):
        self.pname = pname
        self.pid = pid
        self.reads = 0
        self.writes = 0


def main():
    argc = len(sys.argv)
    if argc != 1:
        print("usage: please run this script like [./lyshark.py]")
        sys.exit(0)
    if os.getuid() != 0:
        print("Error: This script must be run as root")
        sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)
    os.system('echo 1 > /proc/sys/vm/block_dump')
    print("TASK              PID       READ      WRITE")
    while True:
        os.system('dmesg -c > /tmp/diskio.log')
        l = []
        f = open('/tmp/diskio.log', 'r')
        line = f.readline()
        while line:
            m = re.match( \
                '^(\S+)(\d+)(\d+): (READ|WRITE) block (\d+) on (\S+)', line)
            if m != None:
                if not l:
                    l.append(DiskIO(m.group(1), m.group(2)))
                    line = f.readline()
                    continue
                found = False
                for item in l:
                    if item.pid == m.group(2):
                        found = True
                        if m.group(3) == "READ":
                            item.reads = item.reads + 1
                        elif m.group(3) == "WRITE":
                            item.writes = item.writes + 1
                if not found:
                    l.append(DiskIO(m.group(1), m.group(2)))
            line = f.readline()
        time.sleep(1)
        for item in l:
            print("%-10s %10s %10d %10d" % \
                  (item.pname, item.pid, item.reads, item.writes))


def signal_handler(signal, frame):
    os.system('echo 0 > /proc/sys/vm/block_dump')
    sys.exit(0)


if __name__ == "__main__":
    main()


#  26.利用Pexpect实现自动非交互登陆linux

# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pexpect
import sys

ssh = pexpect.spawn('ssh root@59.110.167.239')
fout = file('sshlog.log', 'w')
ssh.logfile = fout

ssh.expect("root@59.110.167.239's password:")

ssh.sendline("密码")

ssh.expect('#')
ssh.sendline('ls /home')
ssh.expect('#')


# 27.利用psutil模块获取系统的各种统计信息

import sys
import psutil
import time
import os

# 获取当前时间
time_str = time.strftime("%Y-%m-%d", time.localtime())
file_name = "./" + time_str + ".log"

if os.path.exists(file_name) == False:
    os.mknod(file_name)
    handle = open(file_name, "w")
else:
    handle = open(file_name, "a")

# 获取命令行参数的个数
if len(sys.argv) == 1:
    print_type = 1
else:
    print_type = 2

def isset(list_arr, name):
    if name in list_arr:
        return True
    else:
        return False


print_str = "";


# 获取系统内存使用情况
if (print_type == 1) or isset(sys.argv, "mem"):
    memory_convent = 1024 * 1024
    mem = psutil.virtual_memory()
    print_str += " 内存状态如下:\n"
    print_str = print_str + "   系统的内存容量为: " + str(mem.total / (memory_convent)) + " MB\n"
    print_str = print_str + "   系统的内存以使用容量为: " + str(mem.used / (memory_convent)) + " MB\n"
    print_str = print_str + "   系统可用的内存容量为: " + str(
        mem.total / (memory_convent) - mem.used / (1024 * 1024)) + "MB\n"
    print_str = print_str + "   内存的buffer容量为: " + str(mem.buffers / (memory_convent)) + " MB\n"
    print_str = print_str + "   内存的cache容量为:" + str(mem.cached / (memory_convent)) + " MB\n"


# 获取cpu的相关信息
if (print_type == 1) or isset(sys.argv, "cpu"):
    print_str += " CPU状态如下:\n"
    cpu_status = psutil.cpu_times()
    print_str = print_str + "   user = " + str(cpu_status.user) + "\n"
    print_str = print_str + "   nice = " + str(cpu_status.nice) + "\n"
    print_str = print_str + "   system = " + str(cpu_status.system) + "\n"
    print_str = print_str + "   idle = " + str(cpu_status.idle) + "\n"
    print_str = print_str + "   iowait = " + str(cpu_status.iowait) + "\n"
    print_str = print_str + "   irq = " + str(cpu_status.irq) + "\n"
    print_str = print_str + "   softirq = " + str(cpu_status.softirq) + "\n"
    print_str = print_str + "   steal = " + str(cpu_status.steal) + "\n"
    print_str = print_str + "   guest = " + str(cpu_status.guest) + "\n"


# 查看硬盘基本信息
if (print_type == 1) or isset(sys.argv, "disk"):
    print_str += " 硬盘信息如下:\n"
    disk_status = psutil.disk_partitions()
    for item in disk_status:
        print_str = print_str + "   " + str(item) + "\n"


# 查看当前登录的用户信息
if (print_type == 1) or isset(sys.argv, "user"):
    print_str += " 登录用户信息如下:\n "
    user_status = psutil.users()
    for item in user_status:
        print_str = print_str + "   " + str(item) + "\n"

print_str += "---------------------------------------------------------------\n"
print(print_str)
handle.write(print_str)
handle.close()
# 输出内存使用情况(以字节为单位)

import psutil

mem = psutil.virtual_memory()
print
mem.total, mem.used, mem
print
psutil.swap_memory()  # 输出获取SWAP分区信息


# 输出CPU使用情况

cpu = psutil.cpu_stats()
printcpu.interrupts, cpu.ctx_switches

psutil.cpu_times(percpu=True)  # 输出每个核心的详细CPU信息
psutil.cpu_times().user  # 获取CPU的单项数据 [用户态CPU的数据]
psutil.cpu_count()  # 获取CPU逻辑核心数，默认logical=True
psutil.cpu_count(logical=False)  # 获取CPU物理核心数

# 输出磁盘信息

psutil.disk_partitions()  # 列出全部的分区信息
psutil.disk_usage('/')  # 显示出指定的挂载点情况【字节为单位】
psutil.disk_io_counters()  # 磁盘总的IO个数
psutil.disk_io_counters(perdisk=True)  # 获取单个分区IO个数

# 输出网卡信息
psutil.net_io_counter()
# 获取网络总的IO，默认参数pernic = False
psutil.net_io_counter(pernic=Ture)
# 获取网络各个网卡的IO

# 获取进程信息
psutil.pids()  # 列出所有进程的pid号
p = psutil.Process(2047)
p.name()
# 列出进程名称
p.exe()
# 列出进程bin路径
p.cwd()
# 列出进程工作目录的绝对路径
p.status()
# 进程当前状态[sleep等状态]
p.create_time()
# 进程创建的时间[时间戳格式]
p.uids()
p.gids()
p.cputimes()  # 【进程的CPU时间，包括用户态、内核态】
p.cpu_affinity()  # 显示CPU亲缘关系
p.memory_percent()
# 进程内存利用率
p.meminfo()
# 进程的RSS、VMS信息
p.io_counters()
# 进程IO信息，包括读写IO数及字节数
p.connections()
# 返回打开进程socket的namedutples列表
p.num_threads()
# 进程打开的线程数


# 下面的例子中，Popen类的作用是获取用户启动的应用程序进程信息，以便跟踪程序进程的执行情况

import psutil
from subprocess import PIPE

p = psutil.Popen(["/usr/bin/python", "-c", "print 'helloworld'"], stdout=PIPE)
p.name()
p.username()
p.communicate()
p.cpu_times()

# 其它
psutil.users()  # 显示当前登录的用户，和Linux的who命令差不多

# 获取开机时间
psutil.boot_time()
# 结果是个UNIX时间戳，下面我们来转换它为标准时间格式，如下：
datetime.datetime.fromtimestamp(
    psutil.boot_time())  # 得出的结果不是str格式，继续进行转换 datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d%H:%M:%S')


#28. 生成一个随机密码

# !/usr/bin/env python
# -*- coding:utf-8 -*-
import random, string

def GenPassword(length):
    # 随机出数字的个数
    numOfNum = random.randint(1, length - 1)
    numOfLetter = length - numOfNum

    # 选中numOfNum个数字
    slcNum = [random.choice(string.digits) for i in range(numOfNum)]

    # 选中numOfLetter个字母
    slcLetter = [random.choice(string.ascii_letters) for i in range(numOfLetter)]

    # 打乱这个组合
    slcChar = slcNum + slcLetter
    random.shuffle(slcChar)
    # 生成密码
    genPwd = ''.join([i for i in slcChar])
    return genPwd


if __name__ == '__main__':
    print(GenPassword(6))



# 29.递归下降解析器
import re
import collections

# 定义文本分词变量
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES, DIVIDE, LPAREN, RPAREN, WS]))
Token = collections.namedtuple('Token', ['type', 'value'])


# 过滤文本分词
def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok


class ExpressionEvaluator:
    def parse(self, text):
        self.tokens = generate_tokens(text)
        self.nexttok = None
        self.tok = None
        self._advance()
        return self.expr()

    def _advance(self):
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    def _accept(self, toktype):
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    def _expect(self, toktype):
        if not self._accept(toktype):
            raise SyntaxError('Expected' + toktype)

    def expr(self):
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -= right
        return exprval

    def term(self):
        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval *= right
            elif op == 'DIVIDE':
                termval /= right
        return termval

    def factor(self):
        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')


if __name__ == '__main__':
    e = ExpressionEvaluator()
    print(e.parse('2'))
    print(e.parse('2 + 3'))
    print(e.parse('2 + 3 * 4'))
    print(e.parse('2 + (3 + 4) * 5'))




