import websocket
import threading
import time
# 在接收到服务器发送消息时调用
def on_message(ws, message):
    print('Received: ' + message)

def on_error(ws, exception):
    print('error: ' + exception)

def on_close(ws):
    print("Websocket closed")


# 在和服务器建立完成连接时调用
def on_open(ws):
    # 线程运行函数
    def gao():
        # 往服务器依次发送0-4，每次发送完休息0.01秒
        for i in range(5):
            time.sleep(0.01)
            msg="{0}".format(i)
            ws.send(msg)
            print('Sent: ' + msg)
        #休息5秒用于接收服务器回复的消息
        time.sleep(5)
        # 关闭Websocket的连接
        ws.close()


    # 在另一个线程运行gao()函数
    threading.Thread(target=gao).start()


if __name__ == "__main__":
    ws = websocket.WebSocketApp("ws://echo.websocket.org/",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close,
                              on_open = on_open)

    ws.run_forever()