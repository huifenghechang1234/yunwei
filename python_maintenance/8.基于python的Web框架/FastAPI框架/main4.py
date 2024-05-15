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
声明路径参数的类型
使用 标准的Python类型注释在函数中声明路径参数的类型

输入http://127.0.0.1:8080/items/5555
"""

# 将参数item_id的类型定义为int类型
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

if __name__ == '__main__':
    uvicorn.run(app='main4:app', host="127.0.0.1", port=8080, reload=True)


# 将参数item_name的类型定义为str类型
# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/items/{item_name}")
# def read_item(item_name: str):
#     return {"item_id": item_name}


# if __name__ == '__main__':
#     uvicorn.run(app='main4:app', host="127.0.0.1", port=8080, reload=True)