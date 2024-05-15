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
Response Model(响应模型)

response_model是“ decorator”方法（get，post等）的参数，该参数接受一个模型类。它接收的类型与您
为Pydantic模型属性声明的类型相同，因此它可以是Pydantic模型，但也可以是例如 一个Pydantic模型的清
单，例如List [Item]
"""

from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: List[str] = []

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item




"""
响应模型的使用
第一种、我们可以将请求体的内容全部响应回去
"""

from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.types import EmailStr

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str = None

# Don't do this in production!
@app.post("/user/", response_model=UserIn)
async def create_user(*, user: UserIn):
    return user



"""
第二种情况，将请求体的部分内容响应回去
"""
from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.types import EmailStr
import uvicorn

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None

@app.post("/user/", response_model=UserOut)
async def create_user(*, user: UserIn):
    return user


if __name__ == '__main__':
    uvicorn.run(app='main25:app', host="127.0.0.1", port=8080, reload=True)
