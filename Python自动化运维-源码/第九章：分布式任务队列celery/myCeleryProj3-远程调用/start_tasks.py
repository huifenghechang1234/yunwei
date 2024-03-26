from myCeleryProj.tasks import taskA,taskB
import time
#异步执行 方法一
#resultA = taskA.delay()
#resultB = taskB.delay()

#异步执行 方法一
resultA = taskA.apply_async()
resultB = taskB.apply_async(args=[])
resultC = taskA.apply_async(queue='tasks_B')

while not (resultA.ready() and resultB.ready()):# 循环检查任务是否执行完毕
    time.sleep(1)

print(resultA.successful()) #判断任务是否成功执行
print(resultB.successful()) #判断任务是否成功执行
