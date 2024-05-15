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
深层嵌套模型
可以定义任意深度嵌套的模型
"""

from typing import List, Set

from fastapi import FastAPI
from pydantic import BaseModel, UrlStr

app = FastAPI()

class Image(BaseModel):
    url: UrlStr
    name: str

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: Set[str] = []
    images: List[Image] = None

class Offer(BaseModel):
    name: str
    description: str = None
    price: float
    items: List[Item]

@app.post("/offers/")
async def create_offer(*, offer: Offer):
    return offer
