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
给路径参数添加数字验证：对数字大小
"""
# 第一个，大于或者等于ge，只能比较整数。例如大于等于1

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
        *, item_id: int = Path(..., title="The ID of the item to get", ge=1), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results



# 第二个，小于或者等于le，只能比较整数。例如小于等于1000

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
        *,
        item_id: int = Path(..., title="The ID of the item to get", gt=0, le=1000), q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results




# 第三个，大于gt, 小于lt，可以比较浮点数和整数

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
        *,
        item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
        q: str,
        size: float = Query(..., gt=0, lt=10.5)):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
