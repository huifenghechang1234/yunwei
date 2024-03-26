"""
title = ''
author = 'huifenghechang'
mtime = '2023/12/9'
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
python自动化运维   psutil模块

psutil(python system and process utilities)是一个跨平台的第三方库，用于获取系统运行时的进程
和系统利用率（包括CPU、内存、磁盘、网络等）信息。它主要用于系统监控，性能分析，进程管理等场景
"""
import psutil
import datetime
from subprocess import PIPE

# 1、获取CPU信息
# psutil库可以获取CPU的使用情况。例如，我们可以使用psutil.cpu_percent(interval=1)来
# 获取CPU的使用率。
print("-----------------------1-----------------------------")
print("CPU usage: ", psutil.cpu_percent(interval=1))

# 获取cpu基本信息
cpu_info = psutil.cpu_times()  # 使用psutil.cpu_times()获取CPU的完整信息
print("cpu的基本信息：{}".format(cpu_info))
print("cpu的基本信息：{}".format(type(cpu_info)))  # <class 'psutil._pswindows.scputimes'>

# 获取cpu基本信息中的部分信息
cpu_user = psutil.cpu_times().user
print("cpu执行用户进程的时间占比是：",psutil.cpu_times().user)
print("cpu的系统进程占比信息是：", psutil.cpu_times().system)
print("cpu的dpc信息是：", psutil.cpu_times().dpc)


# 获取cpu的内核基本信息
# 使用psutil.cpu_count()获取CPU逻辑个数
#  cpu_count(,[logical]):默认返回逻辑CPU的个数,当设置logical的参数为False时，返回物理CPU的个数
print("cpu的内核基本信息：", psutil.cpu_count())

# 使用psutil.cpu_count(logical=False)获取CPU的物理个数，默认logical值为True
print("cpu的物理个数是：", psutil.cpu_count(logical=False))  # 默认返回逻辑CPU的个数,当设置logical的参数为False时，返回物理CPU的个数
print("cpu的逻辑个数是：", psutil.cpu_count(logical=True))

"""
cpu_percent(,[percpu],[interval])：返回CPU的利用率
interval：指定的是计算cpu使用率的时间间隔，interval不为0时,则阻塞时显示interval执行的时间内的平均利用率
percpu：指定是选择总的使用率或者每个cpu的使用率,percpu为True时显示所有物理核心的利用率
"""
print("cpu使用率是：", psutil.cpu_percent())   # cpu_percent(,[percpu],[interval])：返回CPU的利用率

# cpu_stats()以命名元组的形式返回CPU的统计信息，包括上下文切换，中断，软中断和系统调用次数
print("cpu的统信息是： ", psutil.cpu_stats())  # cpu_stats()以命名元组的形式返回CPU的统计信息，包括上下文切换，中断，软中断和系统调用次数

# cpu_times_percent(,[percpu])：功能和cpu_times大致相同，看字面意思就能知道，该函数返回的是耗时比例
print("获取耗时比例：", psutil.cpu_times_percent()) # cpu_times_percent

# cpu_freq([percpu])：返回cpu频率
print("cpu频率： ", psutil.cpu_freq()) # cpu_freq
print("------------------------1----------------------------")


print("---------------------2-------------------------------")
# 2、获取内存信息     virtual_memory() 虚拟内存
# 我们可以使用psutil.virtual_memory()来获取系统的内存使用情况。
mem_info = psutil.virtual_memory()
# psutil.virtual_memory():获取系统内存的使用情况，以命名元组的形式返回内存使用情况，包括总内存，可用内存，内存利用率，buffer和cache等。单位为字节
print("虚拟内存基本信息： ", psutil.virtual_memory())

print(f'总虚拟内存 Total memory: {mem_info.total / (1024**3):.2f} GB')
print(f'可用虚拟内存 available: {mem_info.available / (1024**3):.2f} GB')
print(f'空闲虚拟内存 free memory: {mem_info.free / (1024**3):.2f} GB')
print(f'已经使用的虚拟内存 Used memory: {mem_info.used / (1024**3):.2f} GB')
print(f'虚拟内存百分比 : {mem_info.percent}%')


"""
psutil.swap_memory():获取系统交换内存的统计信息，以命名元组的形式返回swap/memory使用情况，包含swap中页的换入和换出。
"""
print("交换内存基本信息：", psutil.swap_memory())

print(f'总交换内存 Total memory: {psutil.swap_memory().total / (1024**3):.2f} GB')
print(f'空闲虚拟内存 free memory: {psutil.swap_memory().free / (1024**3):.2f} GB')
print(f'已经使用的虚拟内存 used memory: {psutil.swap_memory().used / (1024**3):.2f} GB')
print(f'虚拟内存百分比 : {psutil.swap_memory().percent}%')
print("------------------------2----------------------------")


print("------------------------3----------------------------")
# 3、获取磁盘信息
# psutil库也可以获取磁盘的使用情况。例如，我们可以使用psutil.disk_usage(‘/’)来获取
# 根目录的磁盘使用情况。
"""
disk_usage(path)：以命名元组的形式返回path所在磁盘的使用情况，包括磁盘的容量、已经使用的磁盘容量、磁盘的空间利用率等
"""
disk_usage = psutil.disk_usage('/')
print(f'总磁盘挂载点信息 Total disk space: {disk_usage.total / (1024**3):.2f} GB')
print(f'已经使用的磁盘挂载点 Used disk space: {disk_usage.used / (1024**3):.2f} GB')
print(f'磁盘使用挂载点量 Disk usage: {disk_usage.percent}%')

"""
disk_partitions([all=False])：以命名元组的形式返回所有已挂载的磁盘，包含磁盘名称，挂载点，文件系统类型等信息。
当all等于True时，返回包含/proc等特殊文件系统的挂载信息
"""
print("获取磁盘的分区信息: ", psutil.disk_partitions())

"""
disk_io_counters([perdisk])：以命名元组的形式返回磁盘io统计信息(汇总的)，包括读、写的次数，读、写的字节数等。
当perdisk的值为True，则分别列出单个磁盘的统计信息(字典：key为磁盘名称，value为统计的namedtuple)
read_count(读IO数)
write_count(写IO数)
read_bytes(读IO字节数)
write_bytes(写IO字节数)
read_time(磁盘读时间)
write_time(磁盘写时间)
"""
print("获取磁盘io相关信息: ", psutil.disk_io_counters())

print(f"获取磁盘io相关信息: {psutil.disk_io_counters().read_count / (1024**3):.2f} GB")  # 四舍五入
print("获取磁盘io相关信息: ", psutil.disk_io_counters().read_count)
print("获取磁盘单个分区的io个数: ", psutil.disk_io_counters(perdisk=True))
print("------------------------3----------------------------")


print("-----------------------4-----------------------------")
# 4、获取进程信息
# psutil库还可以获取系统中运行的所有进程的信息。例如，我们可以使用psutil.pids()来获取所有进程的PID。
"""
psutil.pids获取系统全部进程
以列表的形式返回当前正在运行的进程
"""
pids = psutil.pids()

# psutil.Process( pid ):对进程进行封装，可以使用该类的方法获取进行的详细信息，或者给进程发送信号。传入参数为pid
print(f'Total processes: {len(pids)}')   # 获取pid的总数

print("pid为8216的进程信息： ", psutil.Process(18636))  # 获取当前指定进程ID
print("进程名: ", psutil.Process(18636).name())  # 进程名
print("进程的bin路径: ", psutil.Process(18636).cwd())  # 进程的bin路径
print("进程的工作目录绝对路径: ", psutil.Process(18636).exe())  # 进程的工作目录绝对路径
print("进程启动的命令行: ", psutil.Process(18636).cmdline())  # 进程启动的命令行
print("父进程ID: ", psutil.Process(18636).ppid())   # 父进程ID
print("父进程: ", psutil.Process(18636).parent())  # 父进程
print("子进程列表: ", psutil.Process(18636).children())  # 子进程列表
print("进程的子进程个数: ", psutil.Process(18636).num_threads())  # 进程的子进程个数
print("进程状态: ", psutil.Process(18636).status())  # 进程状态

date_createtime = datetime.datetime.fromtimestamp(psutil.Process(18636).create_time()).strftime("%Y-%m-%d %H:%M:%S")
print("进程创建时间: ", date_createtime)  # 进程创建时间

# print("进程uid信息: ", psutil.Process(18636).uids())
# print("进程的gid信息： ", psutil.Process(18636).gids())
print("进程使用cpu时间信息,包括user,system两个cpu信息： ", psutil.Process(18636).cpu_times())
print("get进程cpu亲和度,如果要设置cpu亲和度,将cpu号作为参考就好： ", psutil.Process(18636).cpu_affinity())
print("进程内存利用率： ", psutil.Process(18636).memory_percent())
print("进程使用的内存rss,vms信息： ", psutil.Process(18636).memory_info())
print("进程的IO信息,包括读写IO数字及参数： ", psutil.Process(18636).io_counters())
print("进程相关网络连接： ", psutil.Process(18636).connections())
print("进程开启的线程数： ", psutil.Process(18636).num_threads())
print("所有线程信息： ", psutil.Process(18636).threads())
# print("进程终端： ", psutil.Process(17608).terminal())
print("所有线程信息： ", psutil.Process(18636).threads())
print("进程打开的文件： ", psutil.Process(18636).open_files())
print("进程环境变量： ", psutil.Process(18636).environ())
# print("发送SIGTEAM信号结束进程： ", psutil.Process(18636).terminate())
# print("发送SIGKILL信号结束进程： ", psutil.Process(18636).kill())
print("进程是否在运行： ", psutil.Process(18636).is_running())
# print("进程打开的文件个数： ", psutil.Process(18636).num_fds())

"""
popen方法的使用:获取（跟踪）用户启动的应用程序进程信息
基本语法：psutil.Popen([‘执行命令’,‘参数’,‘内容’]，stdout=信息接收器)
属性解析：
exec模式下：[‘执行命令’,‘参数’,‘内容’]
shell模式下： 执行内容 参数 内容
注意：只能在;linux系统下使用
"""
# print("用户进程名称: ", (psutil.Popen(["C:\Users\huifenghechang\AppData\Local\Programs\Python\Python36", "-c", "print('hello')"], stdout=PIPE)).name())
# print("用户进程的启动用户: ", (psutil.Popen(["/usr/bin/python3", "-c", "print('hello')"], stdout=PIPE)).username())
# print("用户进程的连接信息: ", (psutil.Popen(["/usr/bin/python3", "-c", "print('hello')"], stdout=PIPE)).communicate())
# print("用户进程的等待信息: ", (psutil.Popen(["/usr/bin/python3", "-c", "print('hello')"], stdout=PIPE)).wait(timeout=2))


# 其他进程相关的操作
# 1.psutil.pid_exists判断给点定的pid是否存在
print("判断给点定的pid是否存在: ", psutil.pid_exists(18636))

# 2.psutil.process_iter迭代当前正在运行的进程，返回的是每个进程的Process对象
print("返回每个进程的Process对象: ", psutil.process_iter(18636))
print("-------------------------4---------------------------")


print("-------------------------5---------------------------")
# 5.获取网络信息
"""
psutil.net_io_counter([pernic])：以命名元组的形式返回当前系统中每块网卡的网络io统计信息，
包括收发字节数，收发包的数量、出错的情况和删包情况。当pernic为True时，则列出所有网卡的统计信息
"""
print("网络信息io信息：", psutil.net_io_counters())

print("每个网络接口的Io信息：", psutil.net_io_counters(pernic=True))
print("网络信息发送io信息：", psutil.net_io_counters().bytes_sent)
print("网络信息接收io信息：", psutil.net_io_counters().bytes_recv)
print("网络信息发送数据包io信息：", psutil.net_io_counters().packets_sent)
print("网络信息接收数据包io信息：", psutil.net_io_counters().packets_recv)
print("-------------------------5---------------------------")


print("-------------------------6---------------------------")
# 6.获取网卡信息
# psutil.net_if_addrs()：以字典的形式返回网卡的配置信息，包括IP地址和mac地址、子网掩码和广播地址
print("网卡地址信息：", psutil.net_if_addrs())

# psutil.net_if_stats()：返回网卡的详细信息，包括是否启动、通信类型、传输速度与mtu
print("网卡状态信息：", psutil.net_if_stats())

"""
psutil.net_connections()：以列表的形式返回，获取当前网络连接信息
psutil.net_connections([kind]):以列表的形式返回每个网络连接的详细信息(namedtuple)。
命名元组包含fd, family, type, laddr, raddr, status, pid等信息。kind表示过滤的连接类型，
支持的值如下：(默认为inet)
"""
print("网卡连接信息：", psutil.net_connections())
print("-------------------------6---------------------------")


print("-------------------------7---------------------------")
# 7.获取其他信息
print("开机时间：", psutil.boot_time())
date_time_format = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
print("开机时间戳是: {}".format(date_time_format))

# 使用psutil.users()可以获取当前连接的系统用户列表
print("cpu的使用者信息是： ", psutil.users())

# 使用psutil.getloadavg()可以获取平均系统负载,会以元组的形式返回最近1、5和15分钟内的平均系统负载
print("平均系统负载： ", psutil.getloadavg())   # 会以元组的形式返回最近1、5和15分钟内的平均系统负载

# psutil还提供了一个test()方法
# 可以模拟出ps命令的效果
print("test()方法: ", psutil.test())

# Windows services：获取windows的服务
print("获取windows的服务: ", list(psutil.win_service_iter()))

print("alg: ", psutil.win_service_get('alg'))
print("alg.as_dict(): ", psutil.win_service_get('alg').as_dict())
print("-------------------------7---------------------------")



print("-------------------------8---------------------------")
# 8.sensors_传感器
# print("返回硬件的信息: ", psutil.sensors_temperatures())
# print("返回电池状态： ", psutil.sensors_fans())
# print("返回硬件风扇速度： ", psutil.sensors_battery())
# print("返回硬件温度： ", psutil.sensors_temperatures(fahrenheit=False))
print("-------------------------8---------------------------")











