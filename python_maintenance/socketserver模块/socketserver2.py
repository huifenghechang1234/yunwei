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
客户端代码
"""

# !/usr/bin/env python

import socket

HOST = '192.168.1.60'
PORT = 9999

s = socket.socket()
s.connect((HOST, PORT))
while True:
    kel = input('>>>')
    s.sendall(kel)
    print(s.recv(1024))
    if kel == 'exit':
        break
s.close()
