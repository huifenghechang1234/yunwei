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
基于UDP协议，使用socket编写编写一个服务端程序UDP_server.py，一个客户端程
序UDP_client.py，实现客户端和服务端间的通信
"""
import socket


# 1.创建socket对象，指明通信用的协议（ipv4,udp）
def server(server_ip, server_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 指定AF_INET——IPV4和SOCK_DGRAM——UDP协议

    # 2.绑定服务器ip地址和端口，哪个网卡和端口接收和发送数据
    s.bind((server_ip, server_port))

    # 3.只要没退出，就一直接收和发送数据，//收到或者发送的是exit就退出
    while True:
        # 接受数据
        recv_data, cli_addr = s.recvfrom(1024)
        recv_data = recv_data.decode('utf-8')
        print(f"接收：{recv_data}")
        if recv_data == 'exit':
            break
        # 发送数据
        send_data = input("发送：")
        s.sendto(send_data.encode('utf-8'), cli_addr)
        if send_data == 'exit':
            break
    # 4.关闭套接字
    s.close()
