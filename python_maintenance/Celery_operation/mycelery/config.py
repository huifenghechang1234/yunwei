"""
title = ''
author = 'huifenghechang'
mtime = '2024/4/15'
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
配置文件
"""

# 配置文件
# 1. 有redis有密码
# 任务队列的链接地址(变量名必须叫这个)
broker_url = 'redis://:foobared@127.0.0.1:6379/14'
# 结果队列的链接地址(变量名必须叫这个)
result_backend = 'redis://:foobared@127.0.0.1:6379/15'

# 2. redis无密码写法
# 任务队列的链接地址(变量名必须叫这个)
# broker_url = 'redis://127.0.0.1:6379/14'
# 结果队列的链接地址(变量名必须叫这个)
# result_backend = 'redis://127.0.0.1:6379/15'


