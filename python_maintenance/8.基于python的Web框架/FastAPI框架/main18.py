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
创建Schema模型
第一步，从pydantic导入Schema
from pydantic import BaseModel, Schema 

第二步，定义请求体模型并使用Schema模型

注意一点：Schema与 Query，Path和Body的工作方式相同，具有相同的参数
"""

from fastapi import Body, FastAPI
from pydantic import BaseModel, Schema

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = Schema(None, title="The description of the item", max_length=300)
    price: float = Schema(..., gt=0, description="The price must be greater than zero")
    tax: float = None

@app.put("/items/{item_id}")
async def update_item(
        *,
        item_id: int,
        item: Item = Body(..., embed=True)
):
    results = {"item_id": item_id, "item": item}
    return results
