import asyncio
import aiohttp
import time
import requests
import threading

async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    result = await response.text()
    session.close()
    return result


async def request():
    url = "http://127.0.0.1:5000"
    result = await get(url)

start = time.time()
tasks = [asyncio.ensure_future(request()) for _ in range(500)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print( f"协程耗时 {end - start} 秒")



def thread_get():
    url = 'http://127.0.0.1:5000'
    response = requests.get(url)

start = time.time()
ts = []
for i in range(500):
    ts.append(threading.Thread(target=thread_get))
for t in ts:
    t.start()
for t in ts:
    t.join()
end = time.time()
print( f"多线程耗时 {end - start} 秒")

