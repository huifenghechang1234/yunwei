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
使用 Python 编写 grains_module，实现动态配置被控主机 grains的max_open_file 键，值
为ulimit -n的结果，以便动态生成Nginx.conf中的 worker_rlimit_nofile、worker_connections
参数的值，具体代码如下:

我使用了subprocess.run来执行命令，并指定了bash作为shell，以便正确执行source 
/etc/profile && ulimit -n命令。
我使用了stdout.strip()来移除命令输出末尾的空白符，并将其转换为整数。
我将max_open_file的值正确地添加到了grains字典中，使用了grains['max_open_file']
而不是grains('max_open_file')
"""

import subprocess


def NginxGrains():
    """
    返回Nginx配置相关的grains值
    """
    grains = {}
    max_open_file = 65536
    try:
        # 使用subprocess执行命令并获取输出
        result = subprocess.run(['bash', '-c', 'source /etc/profile && ulimit -n'], stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            # 如果命令执行成功，则获取输出并转换为整数
            max_open_file = int(result.stdout.strip())
    except Exception as e:
        # 这里可能需要添加一些错误处理逻辑
        pass

        # 将max_open_file值添加到grains字典中
    grains['max_open_file'] = max_open_file

    return grains


# 调用函数并打印结果
nginx_grains = NginxGrains()
print(nginx_grains)