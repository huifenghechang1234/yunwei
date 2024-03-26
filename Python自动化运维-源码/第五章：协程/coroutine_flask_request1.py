import asyncio
import requests
import time


async def get(url):
    return requests.get(url)


async def request():
    url = "http://127.0.0.1:5000"
    print(f'{time.strftime("%H:%M:%S")} 请求 {url}')
    response = await get(url)
    print(f'{time.strftime("%H:%M:%S")} 得到响应 {response.text}')


start = time.time()
tasks = [asyncio.ensure_future(request()) for _ in range(5)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print(f"耗时 {end - start} 秒")
