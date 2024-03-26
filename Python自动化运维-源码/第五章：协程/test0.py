import asyncio

import time

now = lambda: time.time()

currenttime = lambda : time.strftime('%H:%M:%S')

async def do_some_work(x):
    print(currenttime(),'Waiting: ', x)
    await asyncio.sleep(x)
    return '{} Done after {}s'.format(currenttime(),x)

start = now()

coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)

tasks = [ coroutine1, coroutine2, coroutine3 ]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))


print('TIME: ', now() - start)

