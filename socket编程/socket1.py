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
host = "localhost"
port = 34478

# 绑定地址和端口
server_socket.bind((host, port))

# 开始监听
server_socket.listen(5)
# server_socket.listen(backlog)  backlog为Int整数，表示允许的连接数量，
# 超出的会等待，可以不填，不填会自动设置一个合理值

print("等待客户端连接...")

while True:
    # 建立连接
    client_socket, addr = server_socket.accept()
    # accept方法是阻塞方法，如果没有连接，会卡再当前这一行不向下执行代码
    # accept返回的是一个二元元组，可以使用上述形式，用两个变量接收二元元组的2个元素

    print('连接地址:', addr)
    print("客户端和服务端的连接对象是：", client_socket)

    # 接收客户端发送的数据，要使用客户端和服务端的本次连接对象，而不是socket_server对象
    data: str = client_socket.recv(1024).decode("UTF-8")
    # recv方法的返回值是字节数组(Bytes》，可以通过decode使用UTF-8解码为字符串
    # recv方法的传参是buffsize，缓冲区大小，一般设置为1024即可

    print("接收到客户端的消息:", data.decode())

    # 发送数据到客户端
    client_socket.send("你好，我是服务器！".encode("UTF-8"))
    # encode 可以将字符串编码为字节数组对象

    # 关闭连接
    client_socket.close()
    server_socket.close()  # 关闭socket对象



