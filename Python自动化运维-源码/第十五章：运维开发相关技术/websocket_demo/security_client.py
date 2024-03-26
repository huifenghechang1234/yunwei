import asyncio
import ssl
import pathlib
import websockets

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.load_verify_locations(pathlib.Path(__file__).with_name('localhost.pem'))


async def test_server():
    async with websockets.connect('wss://localhost:8765',ssl = ssl_context) as websocket:
        for data in ["1","2","3","4"]:
            print(f"send data {data}")
            await websocket.send(data)

        for _ in range(4):
            msg = await websocket.recv()
            print(f"received: {msg}")

asyncio.get_event_loop().run_until_complete(test_server())

