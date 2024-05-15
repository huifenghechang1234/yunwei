"""
title = ''
author = 'huifenghechang'
mtime = '2024/1/18'
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
路由route的创建
通过创建路由并关联函数，实现一个基本的网页
"""

from flask import Flask

# 用当前脚本名称实例化Flask对象，方便flask从该脚本文件中获取需要的内容
app = Flask(__name__)


# 程序实例需要知道每个url请求所对应的运行代码是谁。
# 所以程序中必须要创建一个url请求地址到python运行函数的一个映射。
# 处理url和视图函数之间的关系的程序就是"路由"，在Flask中，路由是通过@app.route装饰器(以@开头)来表示的
@app.route("/")
# url映射的函数，要传参则在上述route（路由）中添加参数申明
def index():
    return "Hello World!"


# 直属的第一个作为视图函数被绑定，第二个就是普通函数
# 路由与视图函数需要一一对应
# def not():
#     return "Not Hello World!"

# 启动一个本地开发服务器，激活该网页
app.run()



"""
通过路由的methods指定url允许的请求格式：
"""
#
# from flask import Flask
#
# app = Flask(__name__)
#
#
# # methods参数用于指定允许的请求格式
# # 常规输入url的访问就是get方法
# @app.route("/hello", methods=['GET', 'POST'])
# def hello():
#     return "Hello World!"
#
#
# # 注意路由路径不要重名，映射的视图函数也不要重名
# @app.route("/hi", methods=['POST'])
# def hi():
#     return "Hi World!"
#
#
# app.run()




"""
通过路由在url内添加参数，其关联的函数可以接收该参数：
"""
#
# from flask import Flask
#
# app = Flask(__name__)
#
# # 可以在路径内以/<参数名>的形式指定参数，默认接收到的参数类型是string
#
# '''#######################
# 以下为框架自带的转换器，可以置于参数前将接收的参数转化为对应类型
# string 接受任何不包含斜杠的文本
# int 接受正整数
# float 接受正浮点数
# path 接受包含斜杠的文本
# ########################'''
#
#
# @app.route("/index/<int:id>", )
# def index(id):
#     if id == 1:
#         return 'first'
#     elif id == 2:
#         return 'second'
#     elif id == 3:
#         return 'thrid'
#     else:
#         return 'hello world!'
#
#
# if __name__ == '__main__':
#     app.run()




"""
除了原有的转换器，我们也可以自定义转换器（pip install werkzeug）
"""
#
# from werkzeug.routing import BaseConverter #导入转换器的基类，用于继承方法
# from flask import Flask
#
# app = Flask(__name__)
#
# # 自定义转换器类
# class RegexConverter(BaseConverter):
#     def __init__(self,url_map,regex):
#         # 重写父类定义方法
#         super(RegexConverter,self).__init__(url_map)
#         self.regex = regex
#
#     def to_python(self, value):
#         # 重写父类方法，后续功能已经实现好了
#         print('to_python方法被调用')
#         return value
#
# # 将自定义的转换器类添加到flask应用中
# # 具体过程是添加到Flask类下url_map属性（一个Map类的实例）包含的转换器字典属性中
# app.url_map.converters['re'] = RegexConverter
# # 此处re后括号内的匹配语句，被自动传给我们定义的转换器中的regex属性
# # value值会与该语句匹配，匹配成功则传达给url映射的视图函数
# @app.route("/index/<re('1\d{10}'):value>")
# def index(value):
#     print(value)
#     return "Hello World!"
#
# if __name__=='__main__':
#     app.run(debug=True)
