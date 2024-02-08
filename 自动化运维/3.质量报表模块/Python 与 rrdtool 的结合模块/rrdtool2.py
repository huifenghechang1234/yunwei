"""
title = ''
author = 'huifenghechang'
mtime = '2024/1/3'
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
import rrdtool
import time

# 获取当前 Linux 时间作为 rrd 起始时间
cur_time=str(int(time.time()))
# 数据写频率--step为300秒(即5分钟一个数据点)
rrd=rrdtool.create('Flow.rrd','--step','300','--start',cur_time,
# 定义数据源etho in(入沈量)、etho out(出流量);类型都为COUNTER(递增);600秒为心跳值
# 其含义是 600 秒没有收到值，则会用 UNKNOWN代替:0为最小值:最大值用代替，表示不确定
'DS:eth0 in:COUNTER:600:0:u',
'DS:eth0 out:COUNTER:600:0:U',

# RRA定义格式为[RRA:CF:xffsteps:rows]，CE定义了AVERAGE、MAX、MIN三种数据合并方式
# xff 定义为0.5，表示一个CDP 中的 PDP 值如超过一半值为UNKNOWN，则该CDP 的值就被标为UNKNOWN
# 下列前4个RRA 的定义说明如下，其他定义与AVERAGE 方式相似，区别是存最大值与最小值
# 每隔5分钟(1*300秒)存一次数据的平均值，存 600笔，即2.08天
# 每隔30分钟(6*300秒)存一次数据的平均值，存700笔，即14.58天(2周)
#   每隔2小时(24*300秒)存一次数据的平均值，存775笔，即64.58天(2个月)
#    每隔24 小时 (288*300秒)存一次数据的平均值，存797笔，即797天(2年)
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