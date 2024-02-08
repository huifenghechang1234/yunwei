"""
title = ''
author = 'huifenghechang'
mtime = '2024/2/8'
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
socket服务器端代码
"""

import socket

# 创建一个socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名和端口
host = socket.gethostname()
port = 12345

# 绑定地址和端口
server_socket.bind((host, port))

# 开始监听
server_socket.listen(5)

print("等待客户端连接...")

while True:
    # 建立连接
    client_socket, addr = server_socket.accept()
    print('连接地址:', addr)

    # 接收客户端发送的数据
    data = client_socket.recv(1024)
    print("接收到客户端的消息:", data.decode())

    # 发送数据到客户端
    client_socket.send("你好，我是服务器！".encode())

    # 关闭连接
    client_socket.close()