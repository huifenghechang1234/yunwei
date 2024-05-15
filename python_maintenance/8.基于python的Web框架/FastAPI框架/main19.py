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
额外参数给请求体添加示例字段
将JSON模式示例字段传递给 body请求 JSON模式

当我们访问/docs，我们将看到如下：Example Value | Schema 数据示例，告诉用户，这个api想要
什么样格式的请求体格式数据
"""

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item = Body(
        ...,
        example={ "name": "Foo", "description": "A very nice Item", "price": 35.4, "tax": 3.2, },    )
):
    results = {"item_id": item_id, "item": item}
    return results
