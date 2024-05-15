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
这个应用程序允许用户通过 Web 接口控制定时任务的启动、暂停、恢复和删除。作业信息存储在 
Redis 中，而作业的执行由线程池或进程池处理。这使得应用程序能够处理并发作业，并允许在 
Redis 中持久化作业信息。

这段代码是一个使用 Flask 和 APScheduler 的 Python 应用程序示例。它结合了 Flask
（一个轻量级的 Web 应用框架）和 APScheduler（一个 Python 作业调度库），以实现基于 
Web 的定时任务管理
"""
"""
RedisJobStore：用于将作业信息存储在 Redis 中。
BackgroundScheduler：在后台运行作业的调度器。
ThreadPoolExecutor 和 ProcessPoolExecutor：用于执行作业的线程池和进程池。
Flask 和 make_response：用于构建 Web 应用和生成 HTTP 响应
"""

from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from flask import Flask, make_response

# 创建 Flask 应用实例
app = Flask(__name__)

# 配置Redis作业存储
# 定义一个字典 jobstores，其中包含一个键为 'redis' 的项，使用 RedisJobStore 初始化，并指定 Redis 服务器的地址、端口和数据库
jobstores = {
    'redis': RedisJobStore(host='10.0.0.129', port=6379, db=0, max_connections=10),
}

# 配置执行器
# 定义一个字典 executors，其中包含两个键：'default' 对应一个线程池执行器，'processpool' 对应一个进程池执行器
executors = {
    'default': ThreadPoolExecutor(10),
    'processpool': ProcessPoolExecutor(3),
}

# 调度器配置
# 创建一个 BackgroundScheduler 实例 sched，并传入时区、作业存储和执行器的配置
sched = BackgroundScheduler(timezone='MST', jobstores=jobstores, executors=executors)


# 定义定时任务
# 定义一个函数 my_job，它只打印一条消息 '定时任务'
def my_job():
    print('定时任务')


# 添加定时任务
# 使用 sched.add_job 方法将 my_job 函数添加为定时任务。这个任务每隔 3 秒执行一次，并且有一个宽限时间（misfire_grace_time）为 60 秒
sched.add_job(my_job, 'interval', id='3_second_job', seconds=3, misfire_grace_time=60)


"""
启动调度器的路由
/start：启动调度器。
/pause：暂停调度器中的所有作业。
/resume：恢复调度器中的所有作业。
/remove_job/<job_id>：删除指定 ID 的作业
"""
@app.route('/start')
def start_scheduler():
    if not sched.running:
        sched.start()
    return 'Scheduler started'


# 暂停调度器中所有作业的路由
@app.route('/pause')
def pause_scheduler():
    sched.pause()
    return 'Scheduler paused'


# 恢复调度器中所有作业的路由
@app.route('/resume')
def resume_scheduler():
    sched.resume()
    return 'Scheduler resumed'


# 删除指定作业的路由
@app.route('/remove_job/<job_id>')
def remove_job(job_id):
    if sched.remove_job(job_id):
        return f'Job {job_id} removed'
    else:
        return f'Job {job_id} not found', 404


if __name__ == '__main__':
    # 启动调度器
    sched.start()
    try:
        # 启动Flask应用
        with app.app_context():
            app.run(host="127.0.0.1", port=5000)
    except (KeyboardInterrupt, SystemExit):
        # 捕获Ctrl+C或系统退出信号，以优雅地关闭调度器
        sched.shutdown()