"""
title = ''
author = 'huifenghechang'
mtime = '2024/3/29'
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
分发模块
首先编写分发模块的功能，使用Func的copyle模块来实现，原理比较简单，即读取主
控端 func minion 包下的模块文件(参数传人)，通过Func 的 copy6le 模块同步到目标主机的
同路径下。一次编写可持续使用


请注意以下几点：
导入func.overlord.client时，应使用fc作为别名，而不是fe。
路径字符串中的斜杠应保持一致，且Python版本可能需要根据您的系统进行调整。
使用with open(...) as f:语句可以确保文件正确关闭，这是一种更现代的读取文件内容的方法。
print语句在Python 3中不需要括号，但在Python 2中需要。
重启命令的路径可能因您的系统和安装方式而异，确保使用正确的路径
"""

# !/usr/bin/python
import sys
import func.overlord.client as fc
import xmlrpclib

# 获取命令行参数中的模块名
module = sys.argv[1]

# 修正Python模块路径，注意路径中的斜杠和Python版本
pythonmodulepath = "/usr/lib/python2.6/site-packages/func/minion/modules/"

# 创建Func客户端，连接到所有minions
client = fc.Client("*")

# 读取模块文件内容
with open(pythonmodulepath + module, "r") as f:
    fb = f.read()

# 将文件内容转换为二进制数据
data = xmlrpclib.Binary(fb)

# 分发模块到minions
print(client.system.copyfile(pythonmodulepath + module, data))

# 重启Func服务，注意路径的正确性（通常是/etc/init.d/funcd而不是/ete/init.d/funed）
print(client.system.run("/etc/init.d/funcd restart"))
