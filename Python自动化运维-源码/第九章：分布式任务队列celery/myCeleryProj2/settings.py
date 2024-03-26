from kombu import Queue
import re

CELERY_QUEUES = (  # 定义任务队列
    Queue("default", routing_key="task.#"),  # 路由键以“task.”开头的消息都进default队列
    Queue("tasks_A", routing_key="A.#"),  # 路由键以“A.”开头的消息都进tasks_A队列
    Queue("tasks_B", routing_key="B.#"),  # 路由键以“B.”开头的消息都进tasks_B队列
)

CELERY_TASK_DEFAULT_QUEUE = "default"  # 设置默认队列名为 default
CELERY_TASK_DEFAULT_EXCHANGE = "tasks"
CELERY_TASK_DEFAULT_EXCHANGE_TYPE = "topic"
CELERY_TASK_DEFAULT_ROUTING_KEY = "task.default"

CELERY_ROUTES = (
    [
        (
            re.compile(r"myCeleryProj\.tasks\.(taskA|taskB)"),
            {"queue": "tasks_A", "routing_key": "A.import"},
        ),  # 将tasks模块中的taskA,taskB分配至队列 tasks_A 
        (
            "myCeleryProj.tasks.add",
            {"queue": "default", "routing_key": "task.default"},
        ),  # 将tasks模块中的add任务分配至队列 default
    ],
)


# CELERY_ROUTES = (
#    [
#        ("myCeleryProj.tasks.*", {"queue": "default"}), # 将tasks模块中的所有任务分配至队列 default
#    ],
# )

# CELERY_ROUTES = (
#    [
#        ("myCeleryProj.tasks.add", {"queue": "default"}), # 将add任务分配至队列 default
#        ("myCeleryProj.tasks.taskA", {"queue": "tasks_A"}),# 将taskA任务分配至队列 tasks_A
#        ("myCeleryProj.tasks.taskB", {"queue": "tasks_B"}),# 将taskB任务分配至队列 tasks_B
#    ],
# )

BROKER_URL = "redis://127.0.0.1:6379/0"  # 使用redis 作为消息代理

CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"  # 任务结果存在Redis

CELERY_RESULT_SERIALIZER = "json"  # 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON

CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24  # 任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显


