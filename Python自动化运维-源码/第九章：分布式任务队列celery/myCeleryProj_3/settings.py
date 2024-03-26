from kombu import Queue

#定义任务队列
CELERY_QUEUES = (
        Queue('queueA',routing_key = 'taskA'),
        Queue('queueB',routing_key = 'taskB'),
BROKER_URL = 'redis://127.0.0.1:6379/0'#使用redis 作为消息代理

CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0' # 任务结果存在Redis

CELERY_RESULT_SERIALIZER = 'json' # 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON

CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24 # 任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显

CELERY_TIMEZONE='Asia/Shanghai'
CELERYBEAT_SCHEDULE = {
    "add": {
        "task": "myCeleryProj.tasks.add",
        "schedule": timedelta(seconds=10),#定义间隔为10s的任务
        "args": (10, 16),
    },
    "taskA": {
        "task": "myCeleryProj.tasks.taskA",
        "schedule": crontab(hour=21, minute=11),#定义间隔为对应时区下21：11分执行的任务
    },
    "taskB": {
        "task": "myCeleryProj.tasks.taskB",
        "schedule": crontab(hour=21, minute=8),#定义间隔为对应时区下21：8分执行的任务
    },
}


