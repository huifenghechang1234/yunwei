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
endpoint的作用
说明：每个app中都存在一个url_map，这个url_map中包含了url到endpoint的映射；
作用：当request请求传来一个url的时候，会在url_map中先通过rule找到endpoint，
然后再在view_functions中根据endpoint再找到对应的视图函数view_func

可以通过view_functions查看到当前endpoint与视图函数的对应情况；
可以通过url_map查看当前url与endpoint的绑定情况
"""

from flask import Flask

app = Flask(__name__)


# endpoint默认为视图函数的名称
@app.route('/test')
def test():
    return 'test success!'


# 我们也可以在路由中修改endpoint（当视图函数名称很长时适用）
# 相当于为视图函数起别名
@app.route('/hello', endpoint='our_set')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    print(app.view_functions)
    print(app.url_map)
    app.run()




"""
值得注意的是，endpoint相当于给url起一个名字，view_functions内存储的就是url的名字到视图函数的映射，
且endpoint在同一个蓝图下也不能重名
"""

# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/test', endpoint='Test')
# def test():
#     return 'None'
#
#
# def Test():
#     return 'World!'
#
#
# if __name__ == '__main__':
#     print(app.view_functions)
#     print(app.url_map)
#     app.run()

