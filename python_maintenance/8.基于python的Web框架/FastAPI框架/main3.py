"""
title = ''
author = 'huifenghechang'
mtime = '2024/4/14'
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
Python格式字符串的语法声明路径参数

输入：http://127.0.0.1:8080/items/5555
"""
import uvicorn
from fastapi import FastAPI

# 创建了一个FastAPI应用实例，并将其赋值给变量app。
app = FastAPI()


"""
定义路由和处理函数
@app.get("/items/{item_id}")是一个路由装饰器，它告诉FastAPI当接收到一个路径为
/items/{item_id}的GET请求时，应该调用下面的read_item函数

read_item函数接受一个参数item_id，这个参数的值会自动从请求的URL路径中提取。
函数返回一个字典，其中包含键item_id和对应的值（即路径参数的值
"""
@app.get("/items/{item_id}")
def read_item(item_id):
    return {"item_id": item_id}


if __name__ == '__main__':
    uvicorn.run(app='main3:app', host="127.0.0.1", port=8080, reload=True)