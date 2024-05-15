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
2.主控端扩展模块定制 grains 数据
首先在主控端编写Python代码，然后将该Python文件同步到被控主机，最后刷新生
效(即编译Python源码文件成字节码pyc)。在主控端bash目录(见/etc/salt/master 配置
文件的fle_roots项，默认的basc配置在/srv/salt)下生成_grains目录，执行install -d/
srv/salt/_grains开始编写代码，实现获取被控主机系统允许最大打开文件数(ulimit -n)的
grains 数据


grains_openfile()定义一个获取最大打开文件数的丽数，函数名称没有要求，符合
Python的函数命名规则即可;

grains={}初始化一个grains字典，变量名一定要用grains，以便 Saltstack识别;

grains['max_openfile]= open_file 将获取的 Linux ulimit -n的结果值赋予 grains['max
open file’]，其中“max_open_file”就是grains的项，_open_file 就是 grains 的值
"""

import os
import subprocess


def Grains_openfile():
    """
    返回系统允许打开的最大文件数。
    """
    grains = {}
    # 初始化默认值
    _open_file = 65536  # 这个默认值可能是基于某种特定的系统或配置
    try:
        # 使用subprocess执行命令
        result = subprocess.run(['bash', '-c', 'source /etc/profile && ulimit -n'], stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            # 如果命令执行成功，则解析输出
            _open_file = int(result.stdout.strip())
    except Exception as e:
        pass  # 这里可能需要更详细的错误处理
    grains['max open file'] = _open_file
    return grains


# 使用函数
grains_dict = Grains_openfile()
print(grains_dict)



