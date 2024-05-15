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
返回json数据给前端
"""

"""
方法一：
使用：make_response方法和json库共同完成
"""
# from flask import Flask, make_response, json
#
# app = Flask(__name__)
#
#
# @app.route("/index")
# def index():
#     data = {
#         'name': '张三'
#     }
#     # json.dumps 将一个python数据结构转化为json
#     # json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
#     # 生成一个response响应对象，而不是直接return来返回响应对象，便于执行更多的后续操作
#     response = make_response(json.dumps(data, ensure_ascii=False))
#     # 修改数据的MIME标准类型为json（在发送数据前会先发送该类型）
#     response.mimetype = 'application/json'
#     return response
#
#
# if __name__ == '__main__':
#     app.run()



"""
方法二：
使用：jsonify库实现，减少代码行数
"""
from flask import Flask, jsonify

app = Flask(__name__)
# 在Flask的config是一个存储了各项配置的字典
# 该操作是进行等效于ensure_ascii=False的配置
app.config['JSON_AS_ASCII'] = False


@app.route("/index")
def index():
    data = {
        'name': '张三'
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run()
