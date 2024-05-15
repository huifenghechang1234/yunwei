"""
title = ''
author = 'huifenghechang'
mtime = '2023/11/30'
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
import psutil
import datetime
import time

# 当前时间
now_time = time.strftime('%Y - %m - %d - %H: %M: %S', time.localtime(time.time()))
print(now_time)

# 查看cpu物理个数的信息
print(u"物理CPU个数: %s" % psutil.cpu_count(logical=False))

# cpu的使用率
cpu = (str(psutil.cpu_percent(1))) + '%'
print("cup使用率: %s" %cpu)

# 查看内存信息,剩余内存.free 总共.total
# round() 函数方法为返回浮点数x的四舍五入值。
free = str(round(psutil.virtual_memory().free / (1024.0 * 1024.0 * 1024.0), 2))
total = str(round(psutil.virtual_memory().total / (1024.0 * 1024.0 * 1024.0), 2))
memory = int(psutil.virtual_memory().total - psutil.virtual_memory().free) / float(psutil.virtual_memory().total)
print("物理内存： %sG" %total)
print("剩余物理内存： %sG" %free)
print("物理内存使用率： %s %%" %int(memory * 100))

# 获取系统启动时间
print("系统启动时间: %s" % datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y - %m - %d %H: %M: %S"))

# 获取系统用户
users_count = len(psutil.users())
users_list = ", ".join([u.name for u in psutil.users()])
print("当前有 % s个用户，分别是 % s" %(users_count, users_list))

# 获取网卡信息，可以得到得到网卡属性，连接数，当前数据等信息
net = psutil.net_io_counters()
bytes_sent = "{0: .2f}Mb".format(net.bytes_recv / 1024 / 1024)
bytes_rcvd = "{0: .2f}Mb".format(net.bytes_sent / 1024 / 1024)
print("网卡接收数据 % s网卡发送数据 % s"%(bytes_rcvd, bytes_sent))

# 获取磁盘数据信息
io = psutil.disk_partitions()
print("-----------------------------磁盘信息 - --------------------------------------")

for i in io:
    try:
        o = psutil.disk_usage(i.device)
        print("总容量：" + str(int(o.total / (1024.0 * 1024.0 * 1024.0))) + "G")
        print("已用容量：" + str(int(o.used / (1024.0 * 1024.0 * 1024.0))) + "G")
        print("可用容量：" + str(int(o.free / (1024.0 * 1024.0 * 1024.0))) + "G")
    except PermissionError:
        continue

print("-----------------------------进程信息 - ------------------------------------")

# 查看系统全部进程
for pnum in psutil.pids():
    p = psutil.Process(pnum)
print(
    "进程名 %-20s 内存利用率 %-18s 进程状态 %-10s 创建时间 %-10s " % (
    p.name(), p.memory_percent(), p.status(), p.create_time()))
