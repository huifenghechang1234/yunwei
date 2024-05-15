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
第三步　采用graph方法绘制图表
此示例中关键参数使用了–x-grid定义X轴网格刻度；DEF指定数据源；使用CDEF合并数据；
HRULE绘制水平线（告警线）；GPRINT输出最大值、最小值、平均值等
"""

# !/usr/bin/python
import rrdtool
import time

# 1.定义图表上方大标题
title = "Server network  traffic flow (" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ")"
# 重点解释"--x-grid","MINUTE:12:HOUR:1:HOUR:1:0:%H"参数的作用（从左往右进行分解）

# 2.横坐标定制
"MINUTE:12"  # 表示控制每隔12分钟放置一根次要格线
"HOUR:1"  # 表示控制每隔1小时放置一根主要格线
"HOUR:1"  # 表示控制1个小时输出一个label标签
"0:%H"  # 0表示数字对齐格线，%H表示标签以小时显示

# 3.图形基本格式定制
rrdtool.graph("Flow1.png", "--start", "-1d", "--vertical-label=Bytes/s",
              "--x-grid", "MINUTE:12:HOUR:1:HOUR:1:0:%H",
              "--width", "650", "--height", "230", "--title", title,

              # 4.定制绘图时的基本采样数据
              "DEF:inoctets=Flow.rrd:eth1_in:AVERAGE",  # 指定网卡入流量数据源DS及CF
              "DEF:outoctets=Flow.rrd:eth1_out:AVERAGE",  # 指定网卡出流量数据源DS及CF

              # 5.默认的数据满足不了要求，需要二次处理
              "CDEF:total=inoctets,outoctets,+",  # 通过CDEF合并网卡出入流量，得出总流量total

              # 6.基本数据信息定制
              "LINE1:total#FF8833:Total traffic",  # 以线条方式绘制总流量
              "AREA:inoctets#00FF00:In traffic",  # 以面积方式绘制入流量
              "LINE1:outoctets#0000FF:Out traffic",  # 以线条方式绘制出流量
              "HRULE:6144#FF0000:Alarm value\\r",  # 绘制水平线，作为告警线，阈值为6.1k

              # 7.基本数据展示样式的换算
              "CDEF:inbits=inoctets,8,*",  # 将入流量换算成bit，即*8，计算结果给inbits
              "CDEF:outbits=outoctets,8,*",  # 将出流量换算成bit，即*8，计算结果给outbits

              # 8.注释信息的格式化输出
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



"""
这段代码是一个Python脚本，它使用rrdtool库来生成一个图表，该图表显示了服务器的网络流量情况。RRDtool是一个用于存储、
检索和绘制时间序列数据的开源工具，通常用于系统性能监控。

以下是代码的详细解释：
导入必要的库：
import rrdtool：导入rrdtool库，以便可以使用其提供的绘图和数据处理功能。
import time：导入time库，以便获取当前时间。

定义图表标题：
使用time.strftime('%Y-%m-%d', time.localtime(time.time()))获取当前日期，并将其与固定字符串结合，形成图表的标题。

解释--x-grid参数：
这个参数定义了图表x轴上的网格线。
"MINUTE:12"：每12分钟绘制一个次要的网格线。
"HOUR:1"：每小时绘制一个主要的网格线。
"HOUR:1"：每小时标记一个标签。
"0:%H"：标签的数字与网格线对齐，标签的格式为小时。

使用rrdtool.graph生成图表：
"Flow.png"：生成的图表的文件名。
"--start", "-1d"：图表的数据从昨天开始。
"--vertical-label=Bytes/s"：y轴的标签为"Bytes/s"。
"DEF:inoctets=Flow.rrd:eth1_in:AVERAGE"：定义一个数据源inoctets，它来自Flow.rrd文件的eth1_in数据源，并使用平
均值作为当前的数据点。
"DEF:outoctets=Flow.rrd:eth1_out:AVERAGE"：定义另一个数据源outoctets，它来自Flow.rrd文件的eth1_out数据源。
"CDEF:total=inoctets,outoctets,+"：通过CDEF计算一个新的数据源total，它是入流量和出流量的和。
接下来的几行定义了图表上如何绘制这些数据源：
使用线条绘制总流量。
使用面积图绘制入流量。
使用线条绘制出流量。
绘制一个水平线作为告警线，阈值为6144 Bytes/s。
"CDEF:inbits=inoctets,8,*"和"CDEF:outbits=outoctets,8,*"：将入流量和出流量从字节转换为比特。
接下来的几行定义了图表上的注释和统计数据：
输出换行符。
使用GPRINT绘制入流量和出流量的平均值、最大值和最小值。

最终，这段代码生成了一个名为Flow.png的图表，该图表展示了服务器的网络流量情况，包括入流量、出流量和总流量，以及这些流量
的统计信息
"""