"""
title = ''
author = 'huifenghechang'
mtime = '2023/12/12'
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
# 从modelscope上下载模型
from modelscope.hub.snapshot_download import snapshot_download

model_dir = snapshot_download('baichuan-inc/baichuan-7B', cache_dir='./model', revision='master')
# 如果你网速很好
# ，下载就很快，如果是kb / s，那么大文件下载会失败。