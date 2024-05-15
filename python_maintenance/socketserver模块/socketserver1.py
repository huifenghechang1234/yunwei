"""
title = ''
author = 'huifenghechang'
mtime = '2024/4/6'
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
在socketserver模块中，主要就是使用一些服务器类，从而简化socket网络编程的方法，
先上一段基本的服务器代码
"""

import SocketServer
import time

HOST = '192.168.1.60'
PORT = 9999


class MyHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024)
            print(data, self.client_address)
            self.request.send(' %s %s ' % (data, time.ctime()))
            if data == 'exit':
                break


s = SocketServer.ThreadingTCPServer((HOST, PORT), MyHandler)
s.serve_forever()
