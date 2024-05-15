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
celery执行异步任务
"""

import celery
import time
# backend（后台），就是task result store
backend = 'redis://10.0.0.129:6379/1'
# broker 消息中间件
broker = 'redis://10.0.0.129:6379/2'
# 实例化一个celery对象，test只是个名字，可以任意改
cel = celery.Celery('test', backend=backend, broker=broker)


# 使用celery中的装饰器将函数装饰成celery任务（可能是异步任务，可能是定时任务）
@cel.task
def send_mail(name):
    print('向%s 发送邮件...'%name)
    time.sleep(5)
    print('向%s 发送邮件完成'%name)
    return 'ok'


@cel.task
def send_msg(name):
    print('向%s 发送短信...' % name)
    time.sleep(5)
    print('向%s 发送短信完成' % name)
    return 'ok'



