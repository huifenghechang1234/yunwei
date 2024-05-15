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
分布式 APScheduler
APScheduler 默认是不支持分布式运行的，详见官方 FAQ。当将其集成到 flask 或者 django 项目后，如果用 
gunicorn 部署，gunicorn 可能会启动多个 worker 从而导致 job 重复执行。gunicorn 配置参数 --preload 
和 worker=1 后，只启动一个 worker，可以适当缓解这个问题（这个方法有个问题：当自动重启 worker 的时候，
如果这时后台刚好有一个耗时任务正常执行，比如需要执行 30s，而系统中还有一个每秒执行的任务，这时就会丢失部分
每秒执行的任务）

基本原理：总的来说，其主要是利用 python threading Event 和 Lock 锁来写的。scheduler 在主循环 
（_main_loop）中，反复检查是否有需要执行的任务，完成任务的检查函数为 _process_jobs，这个函数主要有
以下几个步骤
1、 询问储存的每个 jobStore，是否有到期要执行的任务
2、due_jobs 不为空，则计算这些 jobs 中每个 job 需要运行的时间点，时间一到就 submit 给任务调度
3、在主循环中，如果不间断地调用，而实际上没有要执行的 job，这会造成资源浪费。因此在程序中，如果每次掉用
_process_jobs 后，进行了预先判断，判断下一次要执行的 job（离现在最近的）还要多长时间，作为返回值告诉 
main_loop, 这时主循环就可以去睡一觉，等大约这么长时间后再唤醒，执行下一次 _process_jobs

重写 _process_jobs 函数就能解决。主要思路是文件锁，当 worker 准备获取要执行的 job 时必须先获取到文件锁，
获取文件锁后分配 job 到执行器后，再释放文件锁
"""

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.base import MaxInstancesReachedError
from apscheduler.events import (
    JobSubmissionEvent, EVENT_JOB_SUBMITTED, EVENT_JOB_MAX_INSTANCES,
)
from apscheduler.util import (
    timedelta_seconds, TIMEOUT_MAX
)
from datetime import datetime, timedelta
import six
import fcntl
import os

#: constant indicating a scheduler's stopped state
STATE_STOPPED = 0
#: constant indicating a scheduler's running state (started and processing jobs)
STATE_RUNNING = 1
#: constant indicating a scheduler's paused state (started but not processing jobs)
STATE_PAUSED = 2


class DistributedBackgroundScheduler(BackgroundScheduler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _process_jobs(self):
        """
        Iterates through jobs in every jobstore, starts jobs that are due and figures out how long
        to wait for the next round.
        If the ``get_due_jobs()`` call raises an exception, a new wakeup is scheduled in at least
        ``jobstore_retry_interval`` seconds.
        """
        if self.state == STATE_PAUSED:
            self._logger.debug('pid: %s Scheduler is paused -- not processing jobs' % os.getpid())
            return None
        f = None
        try:
            f = open("scheduler.lock", "wb")
            # 这里必须使用 lockf, 因为 gunicorn 的 worker 进程都是 master 进程 fork 出来的
            # flock 会使子进程拥有父进程的锁
            # fcntl.flock(flock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            fcntl.lockf(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
            self._logger.info("pid: %s get Scheduler file lock success" % os.getpid())
        except BaseException as exc:
            self._logger.warning("pid: %s get Scheduler file lock error: %s" % (os.getpid(), str(exc)))
            try:
                if f:
                    f.close()
            except BaseException:
                pass
            return None
        else:
            self._logger.debug('pid: %s Looking for jobs to run' % os.getpid())
            now = datetime.now(self.timezone)
            next_wakeup_time = None
            events = []

            with self._jobstores_lock:
                for jobstore_alias, jobstore in six.iteritems(self._jobstores):
                    try:
                        due_jobs = jobstore.get_due_jobs(now)
                    except Exception as e:
                        # Schedule a wakeup at least in jobstore_retry_interval seconds
                        self._logger.warning('pid: %s Error getting due jobs from job store %r: %s',
                                             os.getpid(), jobstore_alias, e)
                        retry_wakeup_time = now + timedelta(seconds=self.jobstore_retry_interval)
                        if not next_wakeup_time or next_wakeup_time > retry_wakeup_time:
                            next_wakeup_time = retry_wakeup_time

                        continue

                    for job in due_jobs:
                        # Look up the job's executor
                        try:
                            executor = self._lookup_executor(job.executor)
                        except BaseException:
                            self._logger.error(
                                'pid: %s Executor lookup ("%s") failed for job "%s" -- removing it from the '
                                'job store', os.getpid(), job.executor, job)
                            self.remove_job(job.id, jobstore_alias)
                            continue

                        run_times = job._get_run_times(now)
                        run_times = run_times[-1:] if run_times and job.coalesce else run_times
                        if run_times:
                            try:
                                executor.submit_job(job, run_times)
                            except MaxInstancesReachedError:
                                self._logger.warning(
                                    'pid: %s Execution of job "%s" skipped: maximum number of running '
                                    'instances reached (%d)', os.getpid(), job, job.max_instances)
                                event = JobSubmissionEvent(EVENT_JOB_MAX_INSTANCES, job.id,
                                                           jobstore_alias, run_times)
                                events.append(event)
                            except BaseException:
                                # 分配任务错误后马上释放文件锁，让其他 worker 抢占
                                try:
                                    fcntl.flock(f, fcntl.LOCK_UN)
                                    f.close()
                                    self._logger.info("pid: %s unlocked Scheduler file success" % os.getpid())
                                except:
                                    pass
                                self._logger.exception('pid: %s Error submitting job "%s" to executor "%s"',
                                                       os.getpid(), job, job.executor)
                                break
                            else:
                                event = JobSubmissionEvent(EVENT_JOB_SUBMITTED, job.id, jobstore_alias,
                                                           run_times)
                                events.append(event)

                            # Update the job if it has a next execution time.
                            # Otherwise remove it from the job store.
                            job_next_run = job.trigger.get_next_fire_time(run_times[-1], now)
                            if job_next_run:
                                job._modify(next_run_time=job_next_run)
                                jobstore.update_job(job)
                            else:
                                self.remove_job(job.id, jobstore_alias)

                    # Set a new next wakeup time if there isn't one yet or
                    # the jobstore has an even earlier one
                    jobstore_next_run_time = jobstore.get_next_run_time()
                    if jobstore_next_run_time and (next_wakeup_time is None or
                                                   jobstore_next_run_time < next_wakeup_time):
                        next_wakeup_time = jobstore_next_run_time.astimezone(self.timezone)

            # Dispatch collected events
            for event in events:
                self._dispatch_event(event)

            # Determine the delay until this method should be called again
            if next_wakeup_time is None:
                wait_seconds = None
                self._logger.debug('pid: %s No jobs; waiting until a job is added', os.getpid())
            else:
                wait_seconds = min(max(timedelta_seconds(next_wakeup_time - now), 0), TIMEOUT_MAX)
                self._logger.debug('pid: %s Next wakeup is due at %s (in %f seconds)', os.getpid(), next_wakeup_time,
                                   wait_seconds)
            try:
                fcntl.flock(f, fcntl.LOCK_UN)
                f.close()
                self._logger.info("pid: %s unlocked Scheduler file success" % os.getpid())
            except:
                pass

        return wait_seconds
