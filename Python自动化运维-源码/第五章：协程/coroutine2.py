import asyncio
import time

async def task():
    print(f"{time.strftime('%H:%M:%S')} task 开始 ")
    # 异步调用asyncio.sleep(1):
    await  asyncio.sleep(2)
    #time.sleep(2)
    print(f"{time.strftime('%H:%M:%S')} task 结束" )

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
tasks = [task() for _ in range(5)]
start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
end = time.time()
print(f"用时 {end-start} 秒")
