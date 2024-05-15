"""
title = ''
author = 'huifenghechang'
mtime = '2024/4/1'
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
abort函数的使用
什么是abort()？
使用类似于python中的raise函数，可以在需要退出请求的地方抛出错误，并结束该请求；
我们可以使用errorhandler()装饰器来进行异常的捕获与自定义

errorhandler()也可以传入异常类，用于捕获除flask异常列表内的其他异常
"""
from flask import Flask, render_template, request, abort

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        if name == 'zhangsan' and password == '123456':
            return 'login sucess'
        else:
            # abort的用法类似于python中的raise，在网页中主动抛出错误
            abort(404)
            return None



# 自定义错误处理方法,将404这个error与Python函数绑定
# 当需要抛出404error时，将会访问下面的代码
@app.errorhandler(404)
def handle_404_error(err):
    # return "发生了错误，错误情况是：%s"%err
    # 自定义一个界面
    return render_template('404.html')


if __name__ == '__main__':
    app.run()
