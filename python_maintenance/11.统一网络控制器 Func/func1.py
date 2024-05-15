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
自定义模块步骤
如图11-3所示，自定义模块分为四个步骤进行，第一步生成模块，即通过fun-create
module命令创建模块初始模板;第二步编写逻辑，即填充我们的业务功能逻辑，生成模块
第三步分发模块，将编写完成的模块分发到所有被控主机;第四步执行已经分发完成的模块
调用方法与Func自带模块无差异

注意几点：
我将command变量改为了一个列表，这样当shell=False时，Popen可以更安全地执行命令。
我使用decode('utf-8')将返回的二进制数据解码为字符串。这样，当您处理输出时，它将是字符串格式而不是字节格式。
我添加了TODO注释的中文翻译，以帮助理解该函数的预期功能
"""

import func_module
from func.minion import sub_process


class MyModule(func_module.FuncModule):
    # 如果需要，更新这些。
    version = "0.0.1"
    api_version = "0.0.1"
    description = "My module for func."

    def echo(self, vcount):
        """
        TODO: 返回系统消息信息
        """
        command = ["/usr/bin/tail", "-n", str(vcount), "/var/log/messages"]
        cmdref = sub_process.Popen(command, stdout=sub_process.PIPE, stderr=sub_process.PIPE, shell=False,
                                   close_fds=True)
        stdout, stderr = cmdref.communicate()
        return (cmdref.returncode, stdout.decode('utf-8'), stderr.decode('utf-8'))

