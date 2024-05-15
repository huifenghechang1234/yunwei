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
redirect重定向
什么是redirect重定向？
在flask 中，重定向是通过flask.redirect(location, code=302)这个函数来实现的，
location表示需要重定向的url, 应该配合url_for函数来使用， code表示采用哪个重定向，默认是302，
即临时性重定向, 可以修改为301来实现永性重定向；
"""

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/index')
def index():
    # redirect重定位（服务器向外部发起一个请求跳转）到一个url界面；
    # url_for给指定的函数构造 URL；
    # return redirect('/hello') 不建议这样做,将界面限死了
    return redirect(url_for('hello'))

@app.route('/hello')
def hello():
    return 'this is hello fun'

if __name__ == '__main__':
    app.run()

