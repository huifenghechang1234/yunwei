import asyncio
import websockets
import subprocess
from datetime import datetime

async def websocket_server(websocket, path):
    async for command in websocket:
        msg = f"{datetime.now().strftime('%H:%M:%S.%f')[:-3]} received: {command}"
        print(msg)
        await websocket.send(msg)
        cmd_list = command.split(' ')
        try:
            p = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            line = p.stdout.readline().decode('utf8').strip()
            while line:
                await websocket.send(f"{datetime.now().strftime('%H:%M:%S.%f')[:-3]} -> {line}")
                line = p.stdout.readline().decode('utf8').strip()
        except Exception as e:
            print("ERROR: ",e)
            await websocket.send(f"{datetime.now().strftime('%H:%M:%S.%f')[:-3]} ERROR -> {e}")


start_server = websockets.serve(websocket_server, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

