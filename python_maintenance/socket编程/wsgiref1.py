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

"""
from wsgiref.simple_server import make_server

def run(env, response):
    """
    env: 请求相关的所有数据
    response:响应相关的所有数据
    return:返回给浏览器的数据
    """

    print(env) # 返回一个字典，是wsgiref模块自动处理的http的数据

    response('200 ok', [])  # 响应首行，响应头
    current_path = env.get('HTTP_INFO')
    if current_path == '/index':
        return [b'index']
    elif current_path == '/login':
        return [b'login']

    return [b'404 error but hello 卢昱晓']

if __name__ == '__main__':
    server = make_server('127.0.0.1', 8080, run)
    # 会实时监听127.0.0.1:8080地址，只要客户端访问就会交给run函数处理（加括号触发run函数运行）
    server.server_forever()  # 启动服务器