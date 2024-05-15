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
调度器事件
调度器事件只有在某些情况下才会被触发，并且可以携带某些有用的信息。通过 add_listener() 传递适当参数，
可以实现监听不同是事件，比如 job 运行成功、运行失败等

使用 APScheduler 的事件监听器功能来监听任务的执行状态和错误。具体来说，它定义了一个监听器函数 my_listener，
并将其添加到了调度器 scheduler 上，以便在任务执行或发生错误时触发相应的动作
"""
# 导入了两个事件类型：EVENT_JOB_EXECUTED 和 EVENT_JOB_ERROR。前者表示任务执行完成的事件，后者表示任务执行时发生错误的事件
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from apscheduler.schedulers.background import BackgroundScheduler

# 定义监听器函数
"""
my_listener 函数接受一个事件对象 event 作为参数。如果 event 的 exception 属性存在（即任务执行时发生了错误），
则打印出错误信息；否则，打印出任务成功执行的信息
"""


def my_listener(event):
    if event.exception:
        print('The job crashed :(')
    else:
        print('The job worked :)')


scheduler = BackgroundScheduler()
scheduler.start()

"""
添加监听器到调度器
使用 scheduler.add_listener 方法将 my_listener 函数添加到调度器 scheduler 上，并指定它应该监听 
EVENT_JOB_EXECUTED 和 EVENT_JOB_ERROR 这两个事件。这里的 | 运算符用于将两个事件类型进行按位或操作，
从而允许监听器同时监听这两个事件

每当调度器中的任务执行完成或发生错误时，my_listener 函数都会被调用，并根据事件类型打印出相应的信息
"""
scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
