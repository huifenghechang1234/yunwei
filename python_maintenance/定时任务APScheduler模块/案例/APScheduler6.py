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

"""

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR, EVENT_JOB_MISSED
from apscheduler.triggers.cron import CronTrigger
import logging


logger = logging.getLogger('job')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log/TaskChedulerLog.txt',
                    filemode='a',
                    # encoding = 'utf-8', # Python 低版本不支持该配置
                    )


# 重写Cron表达式 提供6个参数进行处理,不支持?
class my_CronTrigger(CronTrigger):
    @classmethod
    def my_from_crontab(cls, expr, timezone="Asia/Shanghai"):
        values = expr.split()
        if len(values) != 6:
            raise ValueError('Wrong number of fields; got {}, expected 7'.format(len(values)))
        return cls(second=values[0], minute=values[1], hour=values[2], day=values[3], month=values[4],
                   day_of_week=values[5], timezone=timezone)


# 定时任务 任务监听器
def my_listener(event):
    job = scheduler.get_job(event.job_id)
    if event.exception:
        logger.info("#### job_error Task error!!!!!!")
        logger.info(event.exception)
        logger.info("#### job_id=%s|obname=%s|jobtrigger=%s|jobtime=%s|retval=%s", event.job_id, job.name, job.trigger,
                    event.scheduled_run_time, event.retval)

    else:
        logger.info('#### jon_normal Task Running...')
        logger.info("#### job_id=%s|jobname=%s|jobtrigger=%s|jobtime=%s|retval=%s", event.job_id, job.name, job.trigger,
                    event.scheduled_run_time, event.retval)


# 定义定时 调度配置
executors = {
    'default': ThreadPoolExecutor(20)
}
job_defaults = {
    'coalesce': True,
    'max_instances': 1
}

# 定时任务 初始化
scheduler = BackgroundScheduler(executors=executors, job_defaults=job_defaults, timezone="Asia/Shanghai")
scheduler.add_listener(my_listener, EVENT_JOB_ERROR | EVENT_JOB_MISSED | EVENT_JOB_EXECUTED)
scheduler._logger = logger

# Cron 6位:* * * * * * 秒、分、时、天、月、周
# project_id,project_name,branch,path,run_env = "1","国内酒店","testSute","/test","dev-test"
# interval_task 为调用Jenkins的函数方法，或也可为调试定时任务执行情况


# scheduler.add_job(interval_task ,my_CronTrigger.my_from_crontab("*/2 * * * * *"),args=[project_name,branch,path,run_env],id=project_id)
# scheduler.add_job(getProJectPlanInfo ,my_CronTrigger.my_from_crontab("*/2 * * * * *"))

# 定义每间隔15分钟更新一次配置，getProJectPlanInfo函数方法为查询数据库定时任务配置筛选启用的定时任务，并对定时任务进行 增、删、改、查操作
scheduler.add_job(getProJectPlanInfo, my_CronTrigger.my_from_crontab("0 */15 * * * *"))

# 显示timing 任务列表
# scheduler.print_jobs(jobstore=None,out=sys.stdout)

scheduler.start()