"""
title = ''
author = 'huifenghechang'
mtime = '2024/4/9'
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
基于TCP协议，使用socket编写编写一个服务端程序TCP_server.py，一个客户端程
序TCP_client.py，实现客户端和服务端间的通信。
"""

# encoding:utf-8
import socket


def recv_send(server_ip, server_port):
    # 1.创建socket对象，指明通信用的协议（ipv4,udp）
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2.绑定ip地址和端口，指明从哪个网卡和端口上接收数据
    s.bind()

    # 3.监听客户端请求
    s.accept()

    # 4.接受客户端请求
    conn, client_adr = s.accept()

    # 5.接收/发送数据
    while True:
        # 接收数据
        recv_data = conn.recv(1024).decode('utf-8')
        print(f"接收:{recv_data}")
        if recv_data == 'exit':
            break

        # 发送数据
        send_data = input("发送:")
        conn.send(send_data.encode('utf-8'))
        if send_data == 'exit':
            break

    # 6.关闭连接
    conn.close()

    # 7.关闭套接字
    s.close()


if __name__ == '__main__':
    server_ip = '127.0.0.1'
    server_port = '5555'
    recv_send(server_ip, server_port)