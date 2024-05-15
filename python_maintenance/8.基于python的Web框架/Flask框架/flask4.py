"""
title = ''
author = 'huifenghechang'
mtime = '2024/3/24'
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
请求钩子before/after_request
想要在正常执行的代码的前、中、后时期，强行执行一段我们想要执行的功能代码，便要用到钩子函数——用特定装饰器装饰的函数
"""

# Flask内，四种常用的钩子：

"""
1.
before_request：在每一次请求之前调用；
该钩子函数表示每一次请求之前，可以执行某个特定功能的函数；
执行顺序是先绑定的先执行；
并且先执行 flask app 的 before_request, 再执行 blueprint 的 before_request；
一般用于检验用户权限、请求是否合法等场景
"""

# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# @app.before_request
# def before_request_a():
#     print('I am in before_request_a')
#
#
# @app.before_request
# def before_request_b():
#     print('I am in before_request_b')
#
#
# if __name__ == '__main__':
#     app.run()




"""
2.
before_first_request：与before_request的区别是，只在第一次请求之前调用；
该钩子函数表示第一次请求之前可以执行的函数；
执行顺序同样也是先绑定的先执行；

"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


# 代码替换视图函数hello_world后，if main前
@app.before_first_request
def teardown_request_a():
    print('I am in teardown_request_a')

@app.before_first_request
def teardown_request_b():
    print('I am in teardown_request_b')

if __name__ == '__main__':
    app.run()



"""
3.
after_request：每一次请求之后都会调用；
该钩子函数表示每一次请求之后，可以执行某个特定功能的函数，这个函数接收response对象，所以执行完后必须归还response对象；
执行的顺序是先绑定的后执行；
被触发的前提是没有异常抛出，或者异常被 errorhandler捕获并处理；
一般可以用于产生csrf_token验证码等场景；
"""
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# # 代码替换视图函数hello_world后，if main前
# @app.after_request
# def after_request_a(response):
#     print('I am in after_request_a')
#     # 该装饰器接收response参数，运行完必须归还response，不然程序报错
#     return response
#
#
# @app.after_request
# def after_request_b(response):
#     print('I am in after_request_b')
#     return response
#
#
# if __name__ == '__main__':
#     app.run()




"""
4.
teardown_request：每一次请求之后都会调用；
该钩子函数接收一个参数，该参数是服务器出现的错误信息；
执行顺序也是先绑定的后执行；
只有在请求上下文被 pop 出请求栈的时候才会直接跳转到teardown_request；
所以在被正常调用之前，即使某次请求有抛出错误，该请求也都会被继续执行, 并在执行完后返回 response；
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


# 代码替换视图函数hello_world后，if main前
@app.after_request
def after_request_a(response):
    print('I am in after_request_a')
    # 该装饰器接收response参数，运行完必须归还response，不然程序报错
    return response


@app.after_request
def after_request_b(response):
    print('I am in after_request_b')
    return response


if __name__ == '__main__':
    app.run()