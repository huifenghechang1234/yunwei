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
request对象的使用
什么是request对象？
render_template()：可以用于呈现一个我们编写的html文件模板
request.method用于获取url接收到的请求方式，以此返回不同的响应页面
"""

# request：包含前端发送过来的所有请求数据

from flask import Flask, render_template, request

# 用当前脚本名称实例化Flask对象，方便flask从该脚本文件中获取需要的内容
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
# url映射的函数，要传参则在上述route（路由）中添加参数申明
def index():
    if request.method == 'GET':
        # 想要html文件被该函数访问到，首先要创建一个templates文件，将html文件放入其中
        # 该文件夹需要被标记为模板文件夹，且模板语言设置为jinja2
        return render_template('index.html')
    # 此处欲发送post请求，需要在对应html文件的form表单中设置method为post
    elif request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        return name + " " + password


if __name__ == '__main__':
    app.run()
