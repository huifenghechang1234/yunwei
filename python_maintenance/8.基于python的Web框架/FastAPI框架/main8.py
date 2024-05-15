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
请求体(Request Body)

使用FastAPI框架和Pydantic库创建的Web API端点。这个端点允许客户端通过POST请求向服务器发送
一个新的Item对象
"""
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

"""
这里定义了一个Item类，它继承自pydantic.BaseModel。这个模型有四个字段：
name: 必需的字符串字段。
description: 可选的字符串字段，默认值为None。
price: 必需的浮点数字段。
tax: 可选的浮点数字段，默认值为None

Pydantic会自动处理这些字段的数据验证和类型转换
"""
class Item(BaseModel):
    name: str
    description: str = 'hello'
    price: float
    tax: float = 3.33


app = FastAPI()


"""
@app.post("/items/")是一个路由装饰器，它告诉FastAPI当接收到一个路径为/items/的POST
请求时，应该调用下面的create_item函数。

create_item函数接受一个参数item，这个参数的类型是前面定义的Item模型。FastAPI会自动将
请求体中的数据解析并验证为Item模型的实例。

函数是异步的（使用了async关键字），这意味着它可以利用异步IO来提高性能，尤其是在处理I/O密集

型任务（如数据库查询或外部API调用）时。
函数返回传入的item对象。在实际应用中，您可能会在这里添加一些业务逻辑，比如将item保存到数据库
"""
@app.post("/items/")
async def create_item(item: Item):
    return item


if __name__ == '__main__':
    uvicorn.run(app='main8:app', host="127.0.0.1", port=8080, reload=True)



"""
使用请求体模型
在函数内部，可以直接访问模型对象的所有属性
"""
# import uvicorn
# from fastapi import FastAPI
# from pydantic import BaseModel
#
#
# class Item(BaseModel):
#     name: str
#     description: str = None
#     price: float
#     tax: float = None
#
#
# app = FastAPI()
#
#
# @app.post("/items/")
# async def create_item(item: Item):
#     return item.name
#
#
# if __name__ == '__main__':
#     uvicorn.run(app='main8:app', host="127.0.0.1", port=8080, reload=True)
