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
查询任务

使用Celery的AsyncResult对象来查询和获取异步任务结果

任务的状态:
PENDING: 任务等待中，尚未被执行。
RETRY: 任务异常后正在重试。
STARTED: 任务已经开始被执行。
以及之前检查过的successful和failed状态

注意：在实际应用中，由于get()方法会阻塞直到任务完成，所以在一个Web请求中直接使用它可能会导致请求超时。因此，
在Web应用中，通常使用回调、轮询或其他机制来异步获取任务结果
"""

from celery_task import app  # 自己写的app

# 从celery.result模块中导入AsyncResult类。这个类用于表示一个异步任务的结果
from celery.result import AsyncResult  # celery模块下的

id = 'b20f827d-dcf5-4fdf-a646-5abb963dc1d3'



if __name__ == '__main__':

    # 创建一个AsyncResult对象a，传入任务的UUID和之前定义的Celery应用实例app
    a = AsyncResult(id=id, app=app)
    if a.successful():

        # 检查任务是否成功完成
        # 如果任务成功完成，调用get()方法来获取任务返回的结果。这个方法会阻塞，直到任务完成并返回结果
        result = a.get()  # task中return的数据:7
        print(result)

    # 检查任务是否失败
    elif a.failed():
        print('任务失败')

    # 通过检查AsyncResult对象的status属性，判断任务的状态，并打印相应的消息
    elif a.status == 'PENDING':
        print('任务等待中，尚未被执行')

    elif a.status == 'RETRY':
        print('任务异常后正在重试')
    elif a.status == 'STARTED':
        print('任务已经开始被执行')
