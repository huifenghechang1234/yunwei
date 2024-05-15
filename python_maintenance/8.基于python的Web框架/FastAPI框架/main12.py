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
参数排序技巧

如果要声明q查询参数而不使用Query或任何默认值，并且使用Path声明路径参数item_id并使用不同的
顺序，则Python对此有一些特殊的语法。

语法规则如下
传递*作为函数的第一个参数。

因为Python不会对第一个星号做任何事情，但是它将知道*星号之后所有参数都应称为关键字参数
（键-值对），也称为kwargs 。 即使它们没有默认值
"""

from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
 *, item_id: int = Path(..., title="The ID of the item to get"), q: str ):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
