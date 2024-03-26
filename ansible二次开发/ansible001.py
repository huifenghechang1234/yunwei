"""
title = ''
author = 'huifenghechang'
mtime = '2024/3/27'
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
) 创建一个带模块参数的简单模块,通过传递进不同的参数内容,显示不同的进程信息;这个模块需要
必须带参数,参数的名字是name,
"""

from ansible.module_utils.basic import *
import commands

# 初始化一个module实例,传递进去的参数里面指定了name为必填项,用required=True修饰
module = AnsibleModule(
    argument_spec=dict(
        name=dict(required=True),
    ),
)
# 获取用户传递进来的name变量
name = module.params['name']

# 根据不同变量,执行任务,输出不同内容
status, output = commands.getstatusoutput('''ps -ef | grep {0}'''.format(name))
if status == 0:
    result = dict(stdout=output, changed=False, rc=0)
    module.exit_json(**result)
else:
    result = dict(msg='execute failed', rc=status)
    module.fail_json(**result)
