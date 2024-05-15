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
声明在URL中出现多次的查询参数
例：http://localhost:8000/items/?q=foo&q=bar
定义：q: List[str] = Query(None)
"""
import uvicorn
from typing import List
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: List[str] = Query(None)):
    query_items = {"q": q}
    return query_items


if __name__ == '__main__':
    uvicorn.run(app='main10:app', host="127.0.0.1", port=8080, reload=True)



"""
设置一个默认值
q: List[str] = Query(["foo", "bar"])
"""
import uvicorn
from typing import List
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: List[str] = Query(["foo", "bar"])):
    query_items = {"q": q}
    return query_items


if __name__ == '__main__':
    uvicorn.run(app='main10:app', host="127.0.0.1", port=8080, reload=True)