"""
title = ''
author = 'huifenghechang'
mtime = '2024/4/8'
code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
┏┓      ┏┓
┏┛┻━━━┛┻┓
┃      ☃      ┃
┃  ┳┛  ┗┳  ┃
┃      ┻      ┃
┗━┓      ┏━┛
┃      ┗━━━┓
┃  神兽保佑    ┣┓
┃　永无BUG！   ┏┛
┗┓┓┏━┳┓┏┛
┃┫┫  ┃┫┫
┗┻┛  ┗┻┛
"""
"""
想模拟一个简单的HTTP服务器。
"""

import socket

server = socket.socket()  # 创建TCP Socket对象
server_address = ('127.0.0.1', 8080)
server.bind(server_address)
server.listen(5)

while True:
    conn, addr = server.accept()
    data = conn.recv(1024)  # 接收数据
    if not data:
        break  # 如果客户端断开连接，则退出循环

    # 解析请求行
    request_line = data.decode('utf-8').splitlines()[0]
    method, path, version = request_line.split(' ')
    current_path = path

    # 构建响应
    response = b'HTTP/1.1 200 OK\r\n'
    response += b'Content-Type: text/html; charset=utf-8\r\n'
    response += b'\r\n'

    if current_path == '/index':
        with open('myhtml.html', 'rb') as f:  # 使用跨平台的路径分隔符
            response += f.read()
    elif current_path == '/login':
        response += b'login'
    else:
        response += b'hello luyuxiao'

        # 发送响应
    conn.sendall(response)
    conn.close()
