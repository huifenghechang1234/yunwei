import asyncio
import websockets

async def test_server():
    # async with websockets.connect('ws://echo.websocket.org') as websocket:
    async with websockets.connect('ws://localhost:8765') as websocket:
        for data in ["1","2","3","4"]:
            print(f"send data {data}")
            await websocket.send(data)

        for _ in range(4):
            msg = await websocket.recv()
            print(f"received: {msg}")

        # async for msg in websocket:
        #     print(f"received: {msg}")


asyncio.get_event_loop().run_until_complete(test_server())

