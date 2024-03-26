import asyncio
import websockets

async def websocket_server(websocket, path):
    async for data in websocket:
    # data = await websocket.recv()
        print(f"received: {data}")
        await websocket.send(data)
        print(f"send: {data}")

start_server = websockets.serve(websocket_server, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

