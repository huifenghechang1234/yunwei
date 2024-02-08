# """
# title = ''
# author = 'huifenghechang'
# mtime = '2023/12/27'
# code is far away from bugs with the god animal protecting
# I love animals. They taste delicious.
# ┏┓      ┏┓
# ┏┛┻━━━┛┻┓
# ┃      ☃      ┃
# ┃  ┳┛  ┗┳  ┃
# ┃      ┻      ┃
# ┗━┓      ┏━┛
# ┃      ┗━━━┓
# ┃  神兽保佑    ┣┓
# ┃　永无BUG！   ┏┛
# ┗┓┓┏━┳┓┏┛
# ┃┫┫  ┃┫┫
# ┗┻┛  ┗┻┛
# """
"""
 介绍
rrdtool（round robin database）工具为环状数据库的存储格式，round robin是一种处理定量
数据以及当前元素指针的技术。rrdtool主要用来跟踪对象的变化情况，生成这些变化的走势图，比如业
务的访问流量、系统性能、磁盘利用率等趋势图，很多流行监控平台都使用到rrdtool，比较有名的为
Cacti、Ganglia、Monitorix等。

rrdtool是一个复杂的工具，涉及较多参数概念，本节主要通过Python的rrdtool模块对rrdtool的
几个常用方法进行封装，包括create、fetch、graph、info、update等方法
"""


import rrdtool
import time, psutil

"""
第一步： create方法创建rrd数据库
采用create方法创建rrd数据库，参数指定了一个rrd文件、更新频率step、起始时间–start、数据源DS、数据源类型DST、数据周期定义RRA等
"""

cur_time = str(int(time.time()))  # 获取当前Linux时间戳作为rrd起始时间
# 数据写频率--step为300秒(即5分钟一个数据点)
rrd = rrdtool.create('Flow.rrd', '--step', '300', '--start', cur_time,
                     # 定义数据源eth1_in(入流量)、eth1_out(出流量)；类型都为COUNTER(递增)；600秒为心跳值，
                     # 其含义是600秒没有收到值，则会用UNKNOWN代替；0为最小值；最大值用U代替，表示不确定
                     'DS:eth1_in:COUNTER:600:0:U',
                     'DS:eth1_out:COUNTER:600:0:U',

                     # RRA定义格式为[RRA:CF:xff:steps:rows]，CF定义了AVERAGE、MAX、MIN三种数据合并方式
                     # xff定义为0.5，表示一个CDP中的PDP值如超过一半值为UNKNOWN，则该CDP的值就被标为UNKNOWN
                     # 下列前4个RRA的定义说明如下，其他定义与AVERAGE方式相似，区别是存最大值与最小值
                     # 每隔5分钟(1*300秒)存一次数据的平均值,存600笔，即2.08天
                     # 每隔30分钟(6*300秒)存一次数据的平均值,存700笔，即14.58天（2周）
                     # 每隔2小时(24*300秒)存一次数据的平均值,存775笔，即64.58天（2个月）
                     # 每隔24小时(288*300秒)存一次数据的平均值,存797笔，即797天(2年)
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
    print
    rrdtool.error()



"""
第二步：采用updatev方法更新rrd数据库
采用updatev方法更新rrd数据库，参数指定了当前的Linux时间戳，以及指定eth0_in、eth0_out值（当前网卡的出入流量），
网卡流量我们通过psutil模块来获取，如psutil.net_io_counters（）[1]为入流量
"""

total_input_traffic = psutil.network_io_counters()[1]  # 获取网卡入流量
total_output_traffic = psutil.network_io_counters()[0]  # 获取网卡出流量
starttime = int(time.time())  # 获取当前Linux时间戳
# 将获取到的三个数据作为updatev的参数，返回{'return_value': 0L}则说明更新成功，反之失败
update = rrdtool.updatev('/root/python/rddtool/Flow.rrd',
                         '%s:%s:%s' % (str(starttime), str(total_input_traffic), str(total_output_traffic)))
print
update


"""
 第三步　采用graph方法绘制图表
此示例中关键参数使用了–x-grid定义X轴网格刻度；DEF指定数据源；使用CDEF合并数据；HRULE绘制水平线（告警线）
；GPRINT输出最大值、最小值、平均值等
"""

# 定义图表上方大标题
title = "Server network  traffic flow (" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ")"
# 重点解释"--x-grid","MINUTE:12:HOUR:1:HOUR:1:0:%H"参数的作用（从左往右进行分解）
"MINUTE:12"  # 表示控制每隔12分钟放置一根次要格线
"HOUR:1"  # 表示控制每隔1小时放置一根主要格线
"HOUR:1"  # 表示控制1个小时输出一个label标签
"0:%H"  # 0表示数字对齐格线，%H表示标签以小时显示
rrdtool.graph("Flow.png", "--start", "-1d", "--vertical-label=Bytes/s",
              "--x-grid", "MINUTE:12:HOUR:1:HOUR:1:0:%H",
              "--width", "650", "--height", "230", "--title", title,
              "DEF:inoctets=Flow.rrd:eth1_in:AVERAGE",  # 指定网卡入流量数据源DS及CF
              "DEF:outoctets=Flow.rrd:eth1_out:AVERAGE",  # 指定网卡出流量数据源DS及CF
              "CDEF:total=inoctets,outoctets,+",  # 通过CDEF合并网卡出入流量，得出总流量total

              "LINE1:total#FF8833:Total traffic",  # 以线条方式绘制总流量
              "AREA:inoctets#00FF00:In traffic",  # 以面积方式绘制入流量
              "LINE1:outoctets#0000FF:Out traffic",  # 以线条方式绘制出流量
              "HRULE:6144#FF0000:Alarm value\\r",  # 绘制水平线，作为告警线，阈值为6.1k
              "CDEF:inbits=inoctets,8,*",  # 将入流量换算成bit，即*8，计算结果给inbits
              "CDEF:outbits=outoctets,8,*",  # 将出流量换算成bit，即*8，计算结果给outbits
              "COMMENT:\\r",  # 在网格下方输出一个换行符
              "COMMENT:\\r",
              "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf %Sbps",  # 绘制入流量平均值
              "COMMENT:   ",
              "GPRINT:inbits:MAX:Max In traffic\: %6.2lf %Sbps",  # 绘制入流量最大值
              "COMMENT:  ",
              "GPRINT:inbits:MIN:MIN In traffic\: %6.2lf %Sbps\\r",  # 绘制入流量最小值
              "COMMENT: ",
              "GPRINT:outbits:AVERAGE:Avg Out traffic\: %6.2lf %Sbps",  # 绘制出流量平均值
              "COMMENT: ",
              "GPRINT:outbits:MAX:Max Out traffic\: %6.2lf %Sbps",  # 绘制出流量最大值
              "COMMENT: ",
              "GPRINT:outbits:MIN:MIN Out traffic\: %6.2lf %Sbps\\r")  # 绘制出流量最小值
