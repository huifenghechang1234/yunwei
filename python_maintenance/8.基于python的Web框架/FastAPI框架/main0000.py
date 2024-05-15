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
使用FastAPI框架定义的一个简单的Web应用

要使这个应用运行起来，您还需要一个ASGI服务器来运行它。常用的ASGI服务器有Uvicorn和Daphne
打开终端，输入运行命令：uvicorn main:app --reload 运行
"""

from fastapi import FastAPI
import uvicorn

app = FastAPI()


# 定义两个路由装饰器@app.get('/')和@app.get("/items/item_id")
"""
第一个路由@app.get('/')对应于应用的根路径/。当访问这个路径时，会调用read_root函数，它返回一
个包含"Hello": "World"的字典。

第二个路由@app.get("/items/item_id")是一个带有路径参数的路由。它期望URL路径中包含一个
item_id，这个item_id将作为整数传递给read_item函数。此外，这个路由还定义了一个可选的查询参
数q，它有一个默认值None。当访问这个路径时（例如/items/123?q=test），会调用read_item函数，
并返回一个包含item_id和q的字典
"""
@app.get('/')
def read_root():
    return {"Hello": "World"}


@app.get("/items/item_id")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    uvicorn.run(app='main0000:app', host="127.0.0.1", port=8080, reload=True)