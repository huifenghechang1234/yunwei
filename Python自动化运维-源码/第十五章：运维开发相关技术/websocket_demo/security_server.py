import asyncio
import pathlib
import ssl
import websockets

async def hello(websocket, path):
    async for data in websocket:
    # data = await websocket.recv()
        print(f"received: {data}")
        await websocket.send(data)
        print(f"send: {data}")

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(
    pathlib.Path(__file__).with_name('localhost.pem'))

start_server = websockets.serve(
    hello, 'localhost', 8765, ssl=ssl_context)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

