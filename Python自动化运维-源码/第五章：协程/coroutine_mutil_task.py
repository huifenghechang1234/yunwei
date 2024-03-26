import asyncio
import requests
import time
async def request():
    url = 'http://www.wjrcb.com'
    status = requests.get(url)
    return status

tasks = [asyncio.ensure_future(request()) for _ in range(100)]
print('Tasks:', tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print(f"{time.strftime('%H:%M:%S')} Task Result:", task.result())