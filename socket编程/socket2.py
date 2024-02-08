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
socket客户端代码
"""

import socket

# 创建一个socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取服务器的主机名和端口
host = socket.gethostname()
port = 12345

# 连接服务器
client_socket.connect((host, port))

# 发送数据到服务器
client_socket.send("你好，我是客户端！".encode())

# 接收服务器的响应
data = client_socket.recv(1024)
print("接收到服务器的消息:", data.decode())

# 关闭连接
client_socket.close()