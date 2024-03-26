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
第一步： create方法创建rrd数据库
采用create方法创建rrd数据库，参数指定了一个rrd文件、更新频率step、起始时间–start、数据源DS、
数据源类型DST、数据周期定义RRA等

绘图步骤：
1 创建数据库
create
2 获取数据
在创建数据库的时候，使用 DS设定数据源
3.更新数据
update命令
4开始绘图
graph
5 重复 2-4
脚本的输出

输入数据的变化率
#获取2秒前后的网卡输入数据
Rx1 = S(ifconfig ens33 | grep 'Rx p' | awk '[print $3}')
sleep 2
Rx2 = S(ifconfig ens33 | grep 'Rx p' | awk '{print $3}')
# 获取数据的变化值
Rx = $(( STX2 - $TX1 ))
# 获取2秒前后的网卡输出数据
Tx1 = S(ifconfig ens33 | grep 'Tx p' | awk '{print $3}')
sleep 2
Tx2 = S(ifconfig ens33 | grep 'Tx p' | awk '{print $3}')
# 获取数据的变化值
Tx = $(( STX2 - $TX1 ))
"""

# -*- coding: utf-8 -*-
# !/usr/bin/python
import rrdtool
import time

cur_time = str(int(time.time()))  # 获取当前Linux时间戳作为rrd起始时间  1.定制的起始时间作为没有必要，因为有默认值now
# 数据写频率--step为300秒(即5分钟一个数据点)
rrd = rrdtool.create('Flow.rrd', '--step', '300', '--start', cur_time,
                     # 定义数据源eth1_in(入流量)、eth1_out(出流量)；类型都为COUNTER(递增)；600秒为心跳值，
                     # 其含义是600秒没有收到值，则会用UNKNOWN代替；0为最小值；最大值用U代替，表示不确定
                     'DS:eth1_in:COUNTER:600:0:U',  # 2.定义两条数据源，输入的数据和输出的数据
                     'DS:eth1_out:COUNTER:600:0:U',

                     # RRA定义格式为[RRA:CF:xff:steps:rows]，CF定义了AVERAGE、MAX、MIN三种数据合并方式
                     # xff定义为0.5，表示一个CDP中的PDP值如超过一半值为UNKNOWN，则该CDP的值就被标为UNKNOWN
                     # 下列前4个RRA的定义说明如下，其他定义与AVERAGE方式相似，区别是存最大值与最小值
                     # 每隔5分钟(1*300秒)存一次数据的平均值,存600笔，即2.08天
                     # 每隔30分钟(6*300秒)存一次数据的平均值,存700笔，即14.58天（2周）
                     # 每隔2小时(24*300秒)存一次数据的平均值,存775笔，即64.58天（2个月）
                     # 每隔24小时(288*300秒)存一次数据的平均值,存797笔，即797天(2年)

                     # 3.定义多种存储样式
                     'RRA:AVERAGE:0.5:1:600',
                     'RRA:AVERAGE:0.5:6:700',
                     'RRA:AVERAGE:0.5:24:775',
                     'RRA:AVERAGE:0.5:288:797',
                     'RRA:MAX:0.5:1:600',
                     'RRA:MAX:0.5:6:700',
                     'RRA:MAX:0.5:24:775',
                     'RRA:MAX:0.5:444:797',
                     'RRA:MIN:0.5:1:600',
                     'RRA:MIN:0.5:6:700',
                     'RRA:MIN:0.5:24:775',
                     'RRA:MIN:0.5:444:797')
if rrd:
    print(rrdtool.error())


"""
这段代码是使用 rrdtool 库的 Python 接口来创建一个 Round Robin Database (RRD) 文件，该文件通常用于存储时间序
列数据，例如网络流量、系统负载、温度等。RRD 是一种特殊类型的数据库，它非常适合存储和检索时间序列数据，尤其是那些需要
定期收集的数据。

下面是对这段代码的详细解释：

1.创建 RRD 文件：
python
rrdtool.create('Flow.rrd', ...)
这行代码开始创建一个名为 Flow.rrd 的 RRD 文件。

2. 设置步长和时间戳：
python
'--step', '300', '--start', cur_time,
* `--step 300`：这表示 RRD 的步长是 300 秒，即每 5 分钟收集一次数据。  
* `--start cur_time`：这表示 RRD 的开始时间戳是 `cur_time`，它应该是一个表示当前时间的 Unix 时间戳。

3. 定义数据源：
python
'DS:eth1_in:COUNTER:600:0:U',  
'DS:eth1_out:COUNTER:600:0:U',
* 这里定义了两个数据源：`eth1_in`（入流量）和 `eth1_out`（出流量）。  
* 数据类型都是 `COUNTER`，表示这些数据是递增的计数器。  
* `600` 是心跳值，表示如果 600 秒内没有收到新的数据值，该数据源的值将被标记为 `UNKNOWN`。  
* `0` 是数据源的最小值。  
* `U` 表示数据源的最大值是不确定的。

4. 定义 RRA（Round Robin Archive）：
python
'RRA:AVERAGE:0.5:1:600',  
'RRA:AVERAGE:0.5:6:700',  
...  
'RRA:MIN:0.5:444:797'
* RRA 用于定义如何存储和检索数据。  
* `RRA:AVERAGE:0.5:1:600`：这表示存储每 5 分钟（1*300 秒）的平均值，并且存储 600 个这样的值。这大约相当于 2.08 
天的数据。  
* `RRA:AVERAGE:0.5:6:700`：每 30 分钟（6*300 秒）存储平均值，存储 700 个值，大约相当于 14.58 天（2 周）的数据。  
* 类似地，后面的 RRA 定义用于存储每 2 小时和每 24 小时的平均值、最大值和最小值。

总的来说，这段代码创建了一个 RRD 文件，该文件将用于存储网络流量数据，包括入流量和出流量，并且定义了如何存储和检索这些数据。
"""

