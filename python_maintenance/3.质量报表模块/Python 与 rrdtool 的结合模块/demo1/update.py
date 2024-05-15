# -*- coding: utf-8 -*-
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
"""
第二步：采用updatev方法更新rrd数据库
采用updatev方法更新rrd数据库，参数指定了当前的Linux时间戳，以及指定eth0_in、eth0_out值
（当前网卡的出入流量），网卡流量我们通过psutil模块来获取，如psutil.net_io_counters（）
[1]为入流量
"""

# !/usr/bin/python
import rrdtool
import time, psutil

# 1.数据的获取方式
# total_input_traffic = psutil.net_io_counters()[1]  # 默认获取网卡入流量
total_input_traffic = psutil.net_io_counters(pernic=True)  # 标准的获取网络流量

total_output_traffic = psutil.net_io_counters()[0]  # 获取网卡出流量
starttime = int(time.time())  # 获取当前Linux时间戳

# 2.数据的更新方式
# 将获取到的三个数据作为updatev的参数，返回{'return_value': 0L}则说明更新成功，反之失败
update = rrdtool.updatev('/python_program/python_maintenance/3.质量报表模块/Python 与 rrdtool 的结合模块/demo1/Flow.rrd',
                         '%s:%s:%s' % (str(starttime), str(total_input_traffic), str(total_output_traffic)))
print(update)
print(starttime)


"""
在这段代码中，你正在使用 psutil 库来获取网络接口的入流量和出流量，并使用 rrdtool 库来更新一个 RRD (Round Robin
Database) 文件，该文件用于存储时间序列数据，如网络流量数据。

首先，代码导入了必要的库：

rrdtool：用于创建、更新和检索 RRD 文件。
time 和 psutil：用于获取当前时间戳和网络流量信息。
然后，代码获取了网络接口的入流量和出流量：

python
total_input_traffic = psutil.net_io_counters()[1]  # 获取网卡入流量  
total_output_traffic = psutil.net_io_counters()[0]  # 获取网卡出流量
请注意，psutil.net_io_counters() 返回一个元组，其中第一个元素是发送的字节数（出流量），第二个元素是接收的字节数
（入流量）。因此，total_input_traffic 和 total_output_traffic 的赋值是反过来的。

接下来，代码获取了当前的 Linux 时间戳：

python
starttime = int(time.time())  # 获取当前Linux时间戳
然后，使用 rrdtool.updatev() 方法来更新 RRD 文件。这个方法接受两个参数：RRD 文件的路径和一个格式化的字符串，该字符
串包含了要更新的时间戳和对应的值。

python
update = rrdtool.updatev('/python_program/python_maintenance/3.质量报表模块/Python 与 rrdtool 的结合模块
/demo1/Flow.rrd',  
                         '%s:%s:%s' % (str(starttime), str(total_input_traffic), 
                         str(total_output_traffic)))
最后，代码打印了更新操作的结果。如果更新成功，update 将包含一个字典，其中包含 'return_value': 0L，表示操作成功。
如果更新失败，update 将包含错误信息。

python
print(update)
这段代码的主要目的是定期更新 RRD 文件以记录网络流量数据，这些数据随后可以用于生成报告或图表来监控网络的使用情况。

确保在运行此代码之前，你已经创建了一个 RRD 文件，并且它的数据源和数据归档设置与你要更新的数据相匹配。此外，请确保 
psutil 和 rrdtool 库已经被正确安装，并且你有权限访问和更新 RRD 文件。
"""