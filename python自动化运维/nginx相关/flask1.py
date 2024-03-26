"""
title = ''
author = 'huifenghechang'
mtime = '2024/3/5'
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
定义了一个Flask应用程序，并创建了几个路由：

/ 路由返回 "Hello, World!" 字符串。
/about 路由返回 "This is the about page." 字符串。
/users/<username> 路由是一个带有变量的路由，它接受一个名为 username 的参数，并使用这个参数来渲染一个名为 user.html 的模板

你可以在Web浏览器中访问 http://127.0.0.1:5000/ 来查看 "Hello, World!" 页面，访问 http://127.0.0.1:5000/about 来查看关
于页面，以及通过访问 http://127.0.0.1:5000/users/<username>（将 <username> 替换为实际用户名）来查看用户个人资料页面
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/about')
def about():
    return 'This is the about page.'


@app.route('/users/<username>')
def show_user_profile(username):
    # 我们将在这里添加一些逻辑来从数据库获取用户信息
    # 假设我们找到了用户，并且他们的信息如下
    user = {'username': username, 'email': 'user@example.com'}
    return render_template('user.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)


