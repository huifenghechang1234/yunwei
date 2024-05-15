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
"""
psutil是一个开源且跨平台（https://code.google.com/p/psutil/）的库，能够轻松实现**获取系统运行的进程和
系统利用率（包括CPU、内存、磁盘、网络等）信息。它主要应用于系统监控，分析和限制系统资源及进程的管理。它实现了
同等命令行工具提供的功能，**如ps、top、lsof、netstat、ifconfig、who、df、kill、free、nice、ionice、
iostat、iotop、uptime、pidof、tty、taskset、pmap等。

在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。还可以跨平台使用，支持Linux／UNIX／OSX／
Windows等，是系统管理员和运维小伙伴不可或缺的必备模块
"""
#  1.获取CPU信息
#  1.1使用psutil.cpu_times()方法
#  使用psutil.cpu_times()获取CPU的完整信息
import psutil
print(psutil.cpu_times())  #scputimes(user=2764.09375, system=1572.8593750000036, idle=28887.218749999996, interrupt=62.015625, dpc=63.515625)
#  scputimes(user=733.23, nice=2.62, system=122.87, idle=19414.35, iowait=29.46, irq=0.0, softirq=34.18, steal=0.0, guest=0.0, guest_nice=0.0)

"""
psutil.cpu_times(percpu=False)解释说明：
以元组的形式返回系统CPU时间。每个属性代表CPU在给定模式下花费的秒数。属性可用性取决于平台：

user: 从系统启动开始累积到当前时刻，处于用户态的运行时间，不包含 nice 值为负的进程。
system: 从系统启动开始累积到当前时刻，处于核心态的运行时间。
idle: 从系统启动开始累积到当前时刻，除 IO 等待时间以外的其他等待时间（空闲时间）。

特定于平台的字段：
nice (UNIX): 系统启动开始累积到当前时刻，nice 值为负的进程所占用的 CPU 时间。Nice值是类UNIX操作系统中表示
静态优先级的数值。 每个进程都有自己的静态优先级，优先级高的进程得以优先运行。
iowait (Linux): 从系统启动开始累积到当前时刻，IO 等待时间。
irq (Linux, BSD): 从系统启动开始累积到当前时刻，服务中断时间
softirq (Linux): 从系统启动开始累积到当前时刻，软中断时间
steal (Linux 2.6.11+): 从系统启动开始累积到当前时刻，在虚拟环境运行时花费在其他操作系统的时间
guest (Linux 2.6.24+):从系统启动开始累积到当前时刻，在Linux内核控制下的操作系统虚拟cpu花费的时间。
guest_nice (Linux 3.2.0+): 从系统启动开始累积到当前时刻，在Linux内核控制下的操作系统虚拟cpu花费在nice进
程上的时间。
interrupt (Windows):从系统启动开始累积到当前时刻，服务硬件中断所花费的时间（类似于UNIX上的“ irq”）
dpc (Windows): 为延迟过程调用（DPC）提供服务所花费的时间；DPC是以低于标准中断的优先级运行的中断
"""

"""
1.2psutil.cpu_count()获取CPU个数
使用psutil.cpu_count()获取CPU逻辑个数
#cpu_count(,[logical]):默认返回逻辑CPU的个数,当设置logical的参数为False时，返回物理CPU的个数。
"""
print(psutil.cpu_count())  # 16


#  使用psutil.cpu_count(logical=False)获取CPU的物理个数，默认logical值为True
